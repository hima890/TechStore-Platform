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

load_dotenv("./.env")

config_name = os.environ.get('FLASK_CONFIG', 'testing')

db = SQLAlchemy()
migrate = Migrate()

jwt = JWTManager()

@jwt.unauthorized_loader
def custom_unauthorized_response(callback):
    return jsonify({
        "status": "error",
        "message": "Missing Authorization Header"
    }), 401

limiter = Limiter(
    get_remote_address,
    default_limits=["200 per day", "50 per hour"],
)

swagger = Swagger()

def create_app():
    """Create the Flask app and initialize it with extensions"""
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(config[config_name])
    
    app.config.from_pyfile('../instance/config.py', silent=True)

    CORS(app, resources={r"/*": {"origins": "*"}})

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    limiter.init_app(app)
    swagger.init_app(app)


    with app.app_context():

        from .models import User, Provider, Store 

        from .apis import (signUp, activation, signIn, optCode,
                           passwordReset, account, store,
                           product, orders)

        app.register_blueprint(signUp)
        app.register_blueprint(activation)
        app.register_blueprint(signIn)
        app.register_blueprint(optCode)
        app.register_blueprint(passwordReset)
        app.register_blueprint(account)
        app.register_blueprint(store)
        app.register_blueprint(product)
        app.register_blueprint(orders)

        db.create_all()

    return app
