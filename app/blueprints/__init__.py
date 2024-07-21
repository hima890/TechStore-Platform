"""
This file is used to create the Flask app and register the blueprints.
"""


from flask import Flask
from config import Config


def create_app(config_class=Config):
    """
    This function is used to create the Flask app and register the blueprints.
    
    Return: The Flask app.
    """
    # Initialize the app
    app = Flask(__name__)

    # Load the configuration
    from blueprints.landingPage.routes.landingPage_route import landingPage
    # Register the blueprints
    app.register_blueprint(landingPage)

    # Return the app
    return app
