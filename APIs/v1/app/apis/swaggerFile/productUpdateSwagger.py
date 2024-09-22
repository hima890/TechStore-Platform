"""Swagger documentation for product update endpoints"""
# product.py

# Documentation for the product update endpoint
productUpdateDoc = {
    'tags': ['Store account Management'],
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': False,
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
            'required': False,
            'description': 'ID of the store'
        },
        {
            'name': 'name',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'description': 'Name of the product'
        },
        {
            'name': 'brand',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'description': 'Brand of the product'
        },
        {
            'name': 'category',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'description': 'Category of the product'
        },
        {
            'name': 'description',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'description': 'Description of the product'
        },
        {
            'name': 'price',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'description': 'Price of the product'
        },
        {
            'name': 'deliveryStatus',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'description': 'Delivery status of the product'
        },
        {
            'name': 'location',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'description': 'Location of the product'
        },
        {
            'name': 'image_1',
            'in': 'formData',
            'schema': {
                'type': 'file'
            },
            'required': False,
            'description': 'Product image'
        }
    ],
    'consumes': [
        'multipart/form-data'
    ],
    'responses': {
        200: {
            'description': 'Product updated successfully.',
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
            'description': 'Bad request or missing token.',
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
            'description': 'Bad request or Provider not found.',
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
