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

# intialize JWTManager
jwt = JWTManager()

# Initialize Flask-Limiter (don't bind to app yet)
limiter = Limiter(
    get_remote_address,  # Function to get client IP address
    default_limits=["200 per day", "50 per hour"],  # Default limits
    # storage_uri="redis://localhost:6379"  # Uncomment if using Redis
)

# Initialize Swagger (don't bind to app yet)
swagger = Swagger()

def create_app():
    """Create the Flask app and initialize it with extensions"""

    # Create the Flask app instance inside the function
    app = Flask(__name__, instance_relative_config=True)

    # Load the configuration from the config.py file
    app.config.from_object(config[config_name])
    
    # Load the configuration from the instance/config.py file (if it exists)
    app.config.from_pyfile('../instance/config.py', silent=True)

    # Initialize extensions with the app
    db.init_app(app)  # Initialize the database
    migrate.init_app(app, db)  # Initialize the migration engine
    jwt.init_app(app)  # Initialize JWT manager
    limiter.init_app(app)  # Initialize the rate limiter
    swagger.init_app(app)  # Initialize Swagger

    # Register blueprints and other app-specific logic here
    with app.app_context():
        # Import models after db is initialized
        from .models import User
        # Import and register the blueprints
        from .apis import signUp, activation, signIn, optCode, store
        app.register_blueprint(signUp)
        app.register_blueprint(activation)
        app.register_blueprint(signIn)
        app.register_blueprint(optCode)
        app.register_blueprint(store)
        
        # Create the database tables
        db.create_all()

    return app
