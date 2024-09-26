#!/usr/bin/python3
""" Flask configuration classes. """
import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv("./.env")

# Define the path to the database file
db_dir = os.path.join(os.getcwd(), 'databases')
db_path = os.path.join(db_dir, 'test_database.db')

# Create the 'databases' directory if it doesn't exist
if not os.path.exists(db_dir):
    os.makedirs(db_dir)


class Config:
    """Base configuration."""
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSONIFY_PRETTYPRINT_REGULAR = True
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    """Development configuration."""
    # Use an environment variable or fall back to 'dev_database.db' by default
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    # Use an environment variable or fall back to 'prod_database.db' by default
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    # Use an environment variable or fall back to 'test_database.db' by default
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    print(SQLALCHEMY_DATABASE_URI)
    TESTING = True
    DEBUG = True


# Declare the configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
