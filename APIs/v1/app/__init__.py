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

# Load environment variables
load_dotenv("./.env")

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

# Custom response for unauthorized access in JWT
@jwt.unauthorized_loader
def custom_unauthorized_response(callback):
    return jsonify({
        "status": "error",
        "message": "Missing Authorization Header"
    }), 401

# Rate limiter setup
limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"],
)


# Swagger setup for API documentation
swagger = Swagger()

def create_app(config_name='production'):
    """Create the Flask app and initialize it with extensions"""
    app = Flask(__name__, instance_relative_config=True)

    # Ensure that config_name is passed as a string ('testing', 'development', etc.)
    app.config.from_object(config[config_name])

    # Optionally load additional instance-specific configuration
    app.config.from_pyfile('../instance/config.py', silent=True)

    # Allow Cross-Origin Resource Sharing (CORS)
    CORS(app, resources={r"/*": {"origins": "*"}})

    # Initialize extensions with the app
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    swagger.init_app(app)
    limiter.init_app(app)

    with app.app_context():
        # Import models to make sure they are registered with SQLAlchemy
        from .models import User, Provider, Store

        # Import and register blueprints for the various APIs
        from .apis import (signUp, activation, signIn, optCode,
                           passwordReset, account, store,
                           product, orders)

        # Import and register the blueprint
        from .routes import main

        # Register all blueprints
        app.register_blueprint(signUp)
        app.register_blueprint(activation)
        app.register_blueprint(signIn)
        app.register_blueprint(optCode)
        app.register_blueprint(passwordReset)
        app.register_blueprint(account)
        app.register_blueprint(store)
        app.register_blueprint(product)
        app.register_blueprint(orders)
        app.register_blueprint(main)

        # Create all tables in the database (if they do not exist)
        db.create_all()

    return app
