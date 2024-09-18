"""Swagger documentation for account password update endpoints"""
# account.py

# Documentation for the update password account endpoint
accountUpdatePasswordDoc = {
    'tags': ['User account Management'],     
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer token' 
        }
        ,
        {
            'name': 'old password',
            'in': 'body',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'new password',
            'in': 'body',
            'type': 'string',
            'required': True
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
        400: {
            'description': 'Bad request, no user token or no data provided.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Token not found.'
                    }
                }
            }
        },
        401: {
            'description': 'Old password is incorrect.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Bad request.'
                    }
                }
            }
        }
    }
}
