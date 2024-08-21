#!/usr/bin/python3
""" Flask Application """
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import config


# Initialize database extensions
db = SQLAlchemy()
migrate = Migrate()
# Get the configuration name from the environment variable, default is testing
config_name = os.environ.get('FLASK_CONFIG', 'testing')


def create_app():
    """Create the Flask app and tells Flask to look for a
    configuration file in the instance/ directory"""
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the configuration from the config.py file
    app.config.from_object(config[config_name])
    
    # Load the configuration from the instance/config.py file (if it exists)
    app.config.from_pyfile('../instance/config.py', silent=True)
    
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from .models import User  # Import models after db is initialized
        from .apis import endPoints
        app.register_blueprint(endPoints)
    # Register blueprints and other app-specific logic here
    
    return app
