"""Sawqer documentation for password reset endpoints"""

# Documentation for the OTP code verification endpoint
resetDoc = {
    'tags': ['Password reset using token'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',  # Set to 'body' to indicate a JSON payload
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'newPassword': {
                        'type': 'string',
                        'example': 'hanafi1234*%^$',
                        'description': 'New account password'
                    }
                },
                'required': ['newPassword']
            }
        }
    ],
    'consumes': [
        'application/json',  # Set the content type to JSON
    ],
    'responses': {
        400: {
            'description': 'Bad request',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'No user token found.'
                    }
                }
            }
        },
        404: {
            'description': 'Bad request',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'No data found in the request.'
                    }
                }
            }
        },
        200: {
            'description': 'Account password reset successful',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        "status": "success",
                        "message": "Password reset successful",
                        "data": {
                            "email": "user email",
                            "username":" user username",
                            "userId": "user id",
                        }
                    }
                }
            }
        }
    }
}
