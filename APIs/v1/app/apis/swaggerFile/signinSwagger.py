"""Sawqer documentation for the login API endpoints"""
# login.py

# Documentation for the login endpoint
siginDoc = {
    'tags': ['User login'],
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
                    },
                    'password': {
                        'type': 'string',
                        'example': 'hima890',
                        'description': 'The password of the user'
                    }
                },
                'required': ['email', 'password']
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
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'User not found.'
                    }
                }
            }
        },
        401: {
            'description': 'Invalid password.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Invalid password.'
                    }
                }
            }
        },
        200: {
            'description': 'Authentication successful',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Authentication successful'
                    },
                    'data': {
                        'type': 'object',
                        'properties': {
                            'email': {
                                'type': 'string',
                                'example': '  [email protected]'
                            },
                            'username': {
                                'type': 'string',
                                'example': 'John Doe'
                            },
                            'userId': {
                                'type': 'integer',
                                'example': 1
                            },
                            'token': {
                                'type': 'string',
                                'example': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFkbWluQGVtYWlsLmNvbSIsImV4cCI6MTU2MjUwNzQyNn0.4x7z4FqRQwU5J3sXg'
                            }
                        }
                    }
                }
            }
        }
    }
}
