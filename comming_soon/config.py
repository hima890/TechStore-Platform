import os
from dotenv import load_dotenv


class ProConfig:
    """
    This class is used to store the configuration of the application.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI') or 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(ProConfig):
    """
    This class is used to store the configuration of the application 
    in the test mode.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
