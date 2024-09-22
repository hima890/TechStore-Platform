"""Swagger documentation for product delete endpoints"""

productDeleteDoc = {
    'tags': ['Store account Management'],
    'summary': 'Delete a product from the store',
    'description': 'Endpoint to delete a product by its ID from the store, accessible to authorized users',
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'schema': {
                'type': 'string'
            },
            'description': 'Bearer token for authentication'
        },
        {
            'name': 'product_id',
            'in': 'formData',
            'required': True,
            'schema': {
                'type': 'integer'
            },
            'description': 'ID of the product to be deleted'
        }
    ],
    'consumes': [
        'application/json'  # Content type for the request
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
