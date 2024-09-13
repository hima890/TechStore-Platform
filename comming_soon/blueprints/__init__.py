from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os
from config import ProConfig, TestConfig

# Load environment variables from .env file
load_dotenv("../.env")

# Determine which config class to use
config_name = ProConfig

# Create the SQLAlchemy object
db = SQLAlchemy()

def create_app(config_class=config_name):
    """
    This function is used to create the Flask app and register the blueprints.
    
    Return: The Flask app.
    """
    # Initialize the app
    app = Flask(__name__)

    # Load the configuration
    app.config.from_object(config_class)

    # Initialize the SQLAlchemy object
    db.init_app(app)

    # Register the blueprints
    from blueprints.landingPage.routes.landingPage_route import landingPage
    app.register_blueprint(landingPage)

    # Create the database
    with app.app_context():
        import models
        db.create_all()

    return app
