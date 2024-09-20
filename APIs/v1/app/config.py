#!/usr/bin/python3
""" Flask configuration classes. """
import os


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
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DEV_DATABASE_URL', 
        'sqlite:///' + os.path.join(os.getcwd(), 'databases', 'dev_database.db')
    )
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    # Use an environment variable or fall back to 'prod_database.db' by default
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'PROD_DATABASE_URL',
        'sqlite:///' + os.path.join(os.getcwd(), 'databases', 'prod_database.db')
    )
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    # Use an environment variable or fall back to 'test_database.db' by default
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'TEST_DATABASE_URL',
        'sqlite:///' + os.path.join(os.getcwd(), 'databases', 'test_database.db')
    )
    print(SQLALCHEMY_DATABASE_URI)
    TESTING = True
    DEBUG = True


# Declare the configuration dictionary
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig
}
