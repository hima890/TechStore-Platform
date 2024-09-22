"""Swagger documentation for product endpoints"""
# account.py

# Documentation for the product endpoint
productDoc = {
    'tags': ['Store account Management'],
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'schema': {
                'type': 'string'
            },
            'description': 'Bearer token for authorization'
        },
        {
            'name': 'storeId',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'ID of the store'
        },
        {
            'name': 'name',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Product name'
        },
        {
            'name': 'brand',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Brand of the product'
        },
        {
            'name': 'category',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Product category'
        },
        {
            'name': 'description',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Product description'
        },
        {
            'name': 'price',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Price of the product'
        },
        {
            'name': 'deliveryStatus',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Delivery status (True/False)'
        },
        {
            'name': 'location',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Location of the product'
        },
        {
            'name': 'image_1',
            'in': 'formData',
            'schema': {
                'type': 'file'
            },
            'required': True,
            'description': 'Product image'
        }
    ],
    'consumes': [
        'multipart/form-data'
    ],
    'responses': {
        200: {
            'description': 'Product information successfully retrieved.',
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
                            'store_id': {
                                'type': 'integer',
                                'example': 1
                            },
                            'name': {
                                'type': 'string',
                                'example': 'Power Bank'
                            },
                            'brand': {
                                'type': 'string',
                                'example': 'AKJ'
                            },
                            'category': {
                                'type': 'string',
                                'example': 'Power'
                            },
                            'description': {
                                'type': 'string',
                                'example': 'High power powerbank'
                            },
                            'price': {
                                'type': 'string',
                                'example': '125.60'
                            },
                            'deliveryStatus': {
                                'type': 'string',
                                'example': 'True'
                            },
                            'image_1': {
                                'type': 'string',
                                'example': 'image_1.png'
                            }
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Bad request, missing user token.',
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
            'description': 'Store not found or bad request.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Store not found.'
                    }
                }
            }
        }
    }
}
