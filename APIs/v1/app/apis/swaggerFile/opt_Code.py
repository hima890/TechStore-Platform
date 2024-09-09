"""Sawqer documentation for the OPT code API endpoints"""

# Documentation for the OPT code endpoint
opt_Code = {
    'tags': ['Password reset by OPT code'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',  # Set to 'body' to indicate a JSON payload
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'email': {
                        'type': 'string',
                        'example': 'hfibrahim90@gmail.com',
                        'description': 'The email of the user'
                    }
                },
                'required': ['email']
            }
        }
    ],
    'consumes': [
        'application/json',  # Set the content type to JSON
    ],
    'responses': {
        404: {
            'description': 'User not found.',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'User not found.'
                    }
                }
            }
        },
        401: {
            'description': 'User acount need to be activated.',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Invalid account.'
                    }
                }
            }
        },
        200: {
            'description': 'OPT code successful',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'OPT code successful'
                    },
                    'data': {
                        'type': 'object',
                        'properties': {
                            'email': {
                                'type': 'string',
                                'example': '  [email protected]'
                            }
                        }
                    }
                }
            }
        }
    }
}
