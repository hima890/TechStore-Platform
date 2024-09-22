createOrderDoc = {
    'tags': ['Order Management'],
    'summary': 'Create a new order',
    'description': 'Create an order by providing order details',
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
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'requester_name': {
                        'type': 'string',
                        'description': 'Name of the customer placing the order',
                        'example': 'John Doe'
                    },
                    'requester_email': {
                        'type': 'string',
                        'description': 'Email of the customer placing the order',
                        'example': 'johndoe@example.com'
                    },
                    'store_id': {
                        'type': 'integer',
                        'description': 'ID of the store processing the order',
                        'example': 1
                    },
                    'title': {
                        'type': 'string',
                        'description': 'Product title',
                        'example': 'Smartphone'
                    },
                    'brand': {
                        'type': 'string',
                        'description': 'Brand of the product',
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
                        'description': 'Quantity of the product ordered',
                        'example': 2
                    },
                    'img': {
                        'type': 'string',
                        'description': 'Optional image of the product',
                        'example': 'smartphone.png'
                    }
                }
            }
        }
    ],
    'consumes': ['application/json'],
    'responses': {
        201: {
            'description': 'Order created successfully.',
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
                            'order_id': {
                                'type': 'integer',
                                'example': 1
                            },
                            'requester_name': {
                                'type': 'string',
                                'example': 'John Doe'
                            },
                            'requester_email': {
                                'type': 'string',
                                'example': 'johndoe@example.com'
                            },
                            'store_id': {
                                'type': 'integer',
                                'example': 1
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
        },
        400: {
            'description': 'Bad request or missing fields.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Missing required fields.'
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
