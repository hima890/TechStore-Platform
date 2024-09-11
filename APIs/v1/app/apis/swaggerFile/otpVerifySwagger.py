"""Sawqer documentation for OTP code verification endpoints"""

# Documentation for the OTP code verification endpoint
verifyDoc = {
    'tags': ['OTP code verification by email'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',  # Set to 'body' to indicate a JSON payload
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'otpCode': {
                        'type': 'string',
                        'example': '658564',
                        'description': 'The OTP code'
                    }
                },
                'required': ['OTPCode']
            }
        }
    ],
    'consumes': [
        'application/json',  # Set the content type to JSON
    ],
    'responses': {
        404: {
            'description': 'Invalid OTP code due to time',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'IInvalid OTP code, time out.'
                    }
                }
            }
        },
        401: {
            'description': 'Invalid OPT code, user not found.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Invalid OPT code.'
                    }
                }
            }
        },
        200: {
            'description': 'OTP code authenticated successful',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        "status": "success",
                        "message": "Authentication successful",
                        "data": {
                            "email": "user email",
                            "username":" user username",
                            "userId": "user id",
                            "token": "user access token"
                        }
                    }
                }
            }
        }
    }
}
