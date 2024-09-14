#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

# Create a Blueprint for the API with the name 'endPoints' and prefix '/api/v1'
signUp = Blueprint('signUp', __name__, url_prefix='/api/v1')
activation = Blueprint('activation', __name__, url_prefix='/api/v1')
signIn = Blueprint('signin', __name__, url_prefix='/api/v1')
optCode = Blueprint('sendOptCode', __name__,  url_prefix='/api/v1')
store = Blueprint('store', __name__, url_prefix='/api/v1/stores')

# Import the API endpoints to register them with the Blueprint
from .signupEndPoint import *
from .userActivationEndPoint import *
from .signinEndPoint import *
from .optCodeEndPoint import *
from .storeEndPoint import *
