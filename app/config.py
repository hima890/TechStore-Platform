import os
from dotenv import load_dotenv

# Get the base directory of the application
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config:
    """
    This class is used to store the configuration of the application.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config):
    """
    This class is used to store the configuration of the application 
    in the test mode.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
