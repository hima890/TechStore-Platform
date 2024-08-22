#!/usr/bin/python3
""" Flask Application """
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from .config import config

# Load environment variables from .env file
load_dotenv("../.env")

# Get the configuration name from the environment variable, default is testing
config_name = os.environ.get('FLASK_CONFIG', 'testing')

# Initialize database extensions and migration engine
db = SQLAlchemy()
migrate = Migrate()

# intialize JWTManager
jwt = JWTManager()


def create_app():
    """Create the Flask app and tells Flask to look for a
    configuration file in the instance/ directory"""
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the configuration from the config.py file
    app.config.from_object(config[config_name])
    
    # Load the configuration from the instance/config.py file (if it exists)
    app.config.from_pyfile('../instance/config.py', silent=True)

    # Config Flask-Limiter to limit the number of requests per user
    limiter = Limiter(
        get_remote_address,  # Function to get client IP address
        app=app,              # Pass the Flask app instance
        default_limits=["200 per day", "50 per hour"]  # Default limits
    )

    # Initialize extensions with the app
    db.init_app(app) # Initialize the database
    migrate.init_app(app, db) # Initialize the migration engine
    jwt.init_app(app)   # Initialize JWT manager
    limiter.init_app(app)  # Initialize the rate limiter

    with app.app_context():
        from .models import User  # Import models after db is initialized
        from .apis import endPoints
        app.register_blueprint(endPoints)
    # Register blueprints and other app-specific logic here
    
    return app
