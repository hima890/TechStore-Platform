productDeleteDoc = {
    'tags': ['Delete product from the provider store'],
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer token for authentication'
        },
        {
            'name': 'product_id',
            'in': 'formData',
            'required': True,
            'type': 'integer',
            'description': 'ID of the product to be deleted'
        }
    ],
    'consumes': [
        'application/json',  # Set the content type for form data
    ],
    'responses': {
        200: {
            'description': 'Product successfully deleted',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Product deleted successfully'
                    }
                }
            }
        },
        400: {
            'description': 'Bad request or missing data',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Bad request, no data provided'
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized request',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Missing or invalid authorization token'
                    }
                }
            }
        },
        404: {
            'description': 'Product or provider not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Product not found'
                    }
                }
            }
        },
        500: {
            'description': 'Internal server error',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Error deleting product or associated images'
                    }
                }
            }
        }
    }
}
