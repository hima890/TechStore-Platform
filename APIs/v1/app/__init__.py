#!/usr/bin/python3
""" Flask Application """
import os
from flask import Flask
from app.apis import endPoints
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config

# Initialize database extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # Get the configuration name from the environment variable, default is testing
    config_name = os.environ.get('FLASK_CONFIG', 'testing')
    """Application factory function."""

    """Create the Flask app and tells Flask to look for a
    configuration file in the instance/ directory"""
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the configuration from the config.py file
    app.config.from_object(config[config_name])
    
    # Load the configuration from the instance/config.py file (if it exists)
    app.config.from_pyfile('config.py', silent=True)
    
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    # Import models to register them with SQLAlchemy
    with app.app_context():
        from . import models
        db.create_all() # Create tables for our models

    # Register blueprints and other app-specific logic here
    app.register_blueprint(endPoints)
    return app
