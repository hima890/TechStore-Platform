"""Sawqer documentation for the user API endpoints"""
# swagger_docs.py

# Documentation for the signup endpoint
signuDoc = {
    'tags': ['User Registration'],
    'parameters': [
        {
            'name': 'username',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'email',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'phone_number',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'type',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'gender',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'location',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
    ],
    'consumes': [
        'multipart/form-data'  # Uncomment this line to use multipart form data
    ],
    'responses': {
        201: {
            'description': 'User created',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'User created! Un email was sent to activate the account.'
                    }
                }
            }
        },
        400: {
            'description': 'Missing fields or user already exists',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Missing fields'
                    }
                }
            }
        },
        409: {
            'description': 'User already exists in the database',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'User already exists'
                    }
                }
            }
        },
        415: {
            'description': 'Request Type must be application/json or multipart/form-data',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Unsupported Request Type'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while creating the user.',
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
        }   }
    }
}
