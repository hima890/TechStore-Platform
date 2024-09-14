"""Swagger documentation for account endpoints"""
# account.py

# Documentation for the account endpoint
accountDoc = {
    'tags': ['User account'],
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer token' 
        }
    ],
    'consumes': [
        'application/json',  # Set the content type to JSON
    ],
    'responses': {
        200: {
            'description': 'User account.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'data': {
                        'type': 'object',
                        'properties': {
                            'userId': {
                                'type': 'integer',
                                'example': 1
                            },
                            'first name': {
                                'type': 'string',
                                'example': 'Hassan'
                            },
                            'last name': {
                                'type': 'string',
                                'example': 'Ibrahim'
                            },
                            'username': {
                                'type': 'string',
                                'example': 'hassan'
                            },
                            'email': {
                                'type': 'string',
                                'example': 'hfibrahim90@gmail.com',
                            },
                            'phone number': {
                                'type': 'string',
                                'example': '08012345678'
                            },
                            'gander': {
                                'type': 'string',
                                'example': 'male'
                            },
                            'location': {
                                'type': 'string',
                                'example': 'Lagos'
                            },
                            'profile image': {
                                'type': 'string',
                                'example': 'profile_image.png'
                            }
                        }
                    }
                }
            }
        },
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
        }
    }
}
