#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

# Create a Blueprint for the API with the name 'endPoints' and prefix '/api/v1'
endPoints = Blueprint('endPoints', __name__, url_prefix='/api/v1')
signUp = Blueprint('signUp', __name__, url_prefix='/api/v1')
activation = Blueprint('activation', __name__, url_prefix='/api/v1')

# Import the API endpoints
from .get_config import *
from .signup import *
from .userActivation import *