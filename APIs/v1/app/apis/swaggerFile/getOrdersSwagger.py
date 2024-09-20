# Swagger documentation for retrieving store orders
getStoreOrdersDoc = {
    'tags': ['Order Management'],     
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer token'
        },
        {
            'name': 'store_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the store whose orders are to be fetched'
        }
    ],
    'responses': {
        200: {
            'description': 'Orders fetched successfully.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'store_id': {
                        'type': 'integer',
                        'example': 1
                    },
                    'store_name': {
                        'type': 'string',
                        'example': 'TechStore'
                    },
                    'orders': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'order_id': {
                                    'type': 'integer',
                                    'example': 1
                                },
                                'name': {
                                    'type': 'string',
                                    'example': 'John Doe'
                                },
                                'email': {
                                    'type': 'string',
                                    'example': 'johndoe@example.com'
                                },
                                'title': {
                                    'type': 'string',
                                    'example': 'Smartphone'
                                },
                                'brand': {
                                    'type': 'string',
                                    'example': 'TechBrand'
                                },
                                'description': {
                                    'type': 'string',
                                    'example': 'Latest model smartphone'
                                },
                                'price': {
                                    'type': 'float',
                                    'example': 599.99
                                },
                                'quantity': {
                                    'type': 'integer',
                                    'example': 2
                                },
                                'total': {
                                    'type': 'float',
                                    'example': 1199.98
                                },
                                'img': {
                                    'type': 'string',
                                    'example': 'smartphone.png'
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Store not found.',
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
