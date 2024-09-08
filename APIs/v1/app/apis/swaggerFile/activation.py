"""Sawqer documentation for the user API endpoints"""
# swagger_docs.py

# Documentation for the activiation endpoint
activation = {
    'tags': ['User activiation'],
    'parameters': [
        {
            'name': 'token',
            'in': 'query',
            'type': 'string',
            'required': False,
            'description': 'Activates a user account using a JWT token provided either as a query parameter.'
        }
        ,
        {
            'name': 'Authorization',
            'in': 'header',
            'type': 'string',
            'required': False,
            'description': 'WT token provided in the Authorization header. Expected format: Bearer <token>'
        }
    ],
    'consumes': [
        'application/json',  # Set the content type to JSON
        'multipart/form-data',  # Uncomment this line to use multipart form data
    ],
    'responses': {
        200: {
            'description': 'Account activated successfully.',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'Account activated successfully.'
                    }
                }
            }
        },
        400: {
            'description': 'Invalid or expired token.',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Invalid or expired token.'
                    }
                }
            }
        },
        401: {
            'description': 'Authorization information is missing or invalid.',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Authorization information is missing or invalid.'
                    }
                }
            }
        },
    }
}
