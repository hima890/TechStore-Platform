#!/usr/bin/python3
""" Flask Application """
import os
from dotenv import load_dotenv
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from redis import Redis
from flasgger import Swagger
from .config import config

# Load environment variables from .env file
load_dotenv("./.env")

# Get the configuration name from the environment variable, default is testing
config_name = os.environ.get('FLASK_CONFIG', 'testing')

# Initialize database extensions and migration engine
db = SQLAlchemy()
migrate = Migrate()

# intialize and Configer JWTManager
jwt = JWTManager()
# Custom error handler for missing token
@jwt.unauthorized_loader
def custom_unauthorized_response(callback):
    return jsonify({
        "status": "error",
        "message": "Missing Authorization Header"
    }), 401

# Create the Flask app instance
app = Flask(__name__, instance_relative_config=True)

# Config Flask-Limiter to limit the number of requests per user
# redis = Redis(host='localhost', port=5007) # Config redis database
limiter = Limiter(
    get_remote_address,  # Function to get client IP address
    app=app,              # Pass the Flask app instance
    default_limits=["200 per day", "50 per hour"],  # Default limits
    # storage_uri="redis://localhost:6379" # Set the uri
)

# Initialize Swagger
swagger = Swagger()

def create_app():
    """This function is used to create the Flask app and register the blueprints.
    
    Return: The Flask app."""
    
    
    # Load the configuration from the config.py file
    app.config.from_object(config[config_name])
    
    # Load the configuration from the instance/config.py file (if it exists)
    app.config.from_pyfile('../instance/config.py', silent=True)

    # Enable CORS for all routes and all origins
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Initialize extensions with the app
    db.init_app(app) # Initialize the database
    migrate.init_app(app, db) # Initialize the migration engine
    jwt.init_app(app)   # Initialize JWT manager
    limiter.init_app(app)  # Initialize the rate limiter
    swagger.init_app(app)     # Initialize Swagger

    # Register blueprints and other app-specific logic here
    with app.app_context():
        # Import tabels after db is initialized
        from .models import User
        # Import the end-point
        from .apis import (signUp, activation, signIn, optCode, passwordReset, account)
        # Register the end-pointe
        app.register_blueprint(signUp)
        app.register_blueprint(activation)
        app.register_blueprint(signIn)
        app.register_blueprint(optCode)
        app.register_blueprint(passwordReset)
        app.register_blueprint(account)
        # Create the database tabels
        db.create_all()

    return app
