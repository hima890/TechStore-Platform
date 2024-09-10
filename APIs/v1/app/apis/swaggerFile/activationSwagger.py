"""Sawqer documentation for the user API endpoints"""
# swagger_docs.py

# Documentation for the activiation endpoint
activiationDoc = {
    'tags': ['User Activation'],
    'description': 'Activate user account by submitting the token received via email in JSON format.',
    'parameters': [
        {
            'name': 'body',
            'in': 'path',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'token': {
                        'type': 'string',
                        'description': 'The token sent to the user via email for account activation.',
                        'example': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...',
                        'required': True
                    }
                }
            }
        }
    ],
    'consumes': [
        'application/json'
    ],
    'responses': {
        200: {
            'description': 'Account activated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Account successfully activated.'
                    }
                }
            }
        },
        400: {
            'description': 'Invalid or expired token',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Invalid token'
                    }
                }
            }
        },
        404: {
            'description': 'User not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'User not found'
                    }
                }
            }
        },
        500: {
            'description': 'Internal Server Error',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Internal Server Error'
                    }
                }
            }
        }
    }
}
