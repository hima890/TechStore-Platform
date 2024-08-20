#!/usr/bin/python3
""" Flask Application """
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from ..instance import config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name):
    """Application factory function."""
    app = Flask(__name__, instance_relative_config=True)
    
    # Load the configuration from the config.py file
    app.config.from_object(config[config_name])
    
    # Load the configuration from the instance/config.py file (if it exists)
    app.config.from_pyfile('config.py', silent=True)
    
    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # Register blueprints and other app-specific logic here
    
    return app
