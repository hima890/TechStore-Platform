#!/usr/bin/python3
""" get the configuration for the current environment """
from . import endPoints
from ..config import Config


# Create a route to get the configuration
# The strict_slashes parameter allows the route to match a URL with or without a trailing slash
@endPoints.route('/config', methods=['GET'], strict_slashes=False)
def get_config():
    """ Get the configuration for the current environment """
    # Get the configuration from the app's configuration
    return {
        'SECRET_KEY': str(Config.SECRET_KEY),
    }
