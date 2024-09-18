"""Swagger documentation for account update endpoints"""
# account.py

# Documentation for the update account endpoint
accountUpdateDoc = {
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
            'name': 'first_name',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'last_name',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'username',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'email',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'phone_number',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'type',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'gender',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'location',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'profile_image',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Optional profile image for the user'
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
            'description': 'Bad request, no user token.',
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
        404: {
            'description': 'Bad request or User not found.',
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
