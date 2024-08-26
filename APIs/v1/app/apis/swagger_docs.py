# swagger_docs.py

signup_doc = {
    'tags': ['User Registration'],
    'parameters': [
        {
            'name': 'username',
            'in': 'formData',
            'type': 'string',
            'required': True
        },
        {
            'name': 'email',
            'in': 'formData',
            'type': 'string',
            'required': True
        },
        {
            'name': 'password',
            'in': 'formData',
            'type': 'string',
            'required': True
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
        # 'application/json',  # Set the content type to JSON
        'multipart/form-data',  # Uncomment this line to use multipart form data
    ],
    'responses': {
        200: {
            'description': 'User registered successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'message': {
                        'type': 'string',
                        'example': 'User registered successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Missing fields or user already exists',
            'schema': {
                'type': 'object',
                'properties': {
                    'error': {
                        'type': 'string',
                        'example': 'Missing fields'
                    }
                }
            }
        }
    }
}
