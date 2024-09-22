getStoreOrdersDoc = {
    'tags': ['Order Management'],
    'summary': 'Retrieve orders for a specific store',
    'description': 'Fetch all orders for a store based on its store_id',
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
            'name': 'store_id',
            'in': 'path',
            'required': True,
            'schema': {
                'type': 'integer'
            },
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
                                'requester_name': {
                                    'type': 'string',
                                    'description': 'Name of the user who requested the order',
                                    'example': 'John Doe'
                                },
                                'requester_email': {
                                    'type': 'string',
                                    'description': 'Email of the user who requested the order',
                                    'example': 'johndoe@example.com'
                                },
                                'title': {
                                    'type': 'string',
                                    'description': 'Product title',
                                    'example': 'Smartphone'
                                },
                                'brand': {
                                    'type': 'string',
                                    'description': 'Product brand',
                                    'example': 'TechBrand'
                                },
                                'description': {
                                    'type': 'string',
                                    'description': 'Product description',
                                    'example': 'Latest model smartphone'
                                },
                                'price': {
                                    'type': 'float',
                                    'description': 'Product price',
                                    'example': 599.99
                                },
                                'quantity': {
                                    'type': 'integer',
                                    'description': 'Quantity ordered',
                                    'example': 2
                                },
                                'total': {
                                    'type': 'float',
                                    'description': 'Total price of the order',
                                    'example': 1199.98
                                },
                                'img': {
                                    'type': 'string',
                                    'description': 'Image of the product',
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
