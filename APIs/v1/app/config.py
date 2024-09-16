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
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        os.getcwd(),
        'APIs/v1/'
        'databases',
        'test_database.db'
        )
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        os.getcwd(),
        'APIs/v1/'
        'databases',
        'test_database.db'
        )
    DEBUG = False


class TestingConfig(Config):
    """Testing configuration."""
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        os.getcwd(),
        'APIs/v1/'
        'databases',
        'test_database.db'
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
