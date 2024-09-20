# Swagger documentation for the create order endpoint
createOrderDoc = {
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
            'name': 'name',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Customer name'
        },
        {
            'name': 'email',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Customer email'
        },
        {
            'name': 'store_id',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'ID of the store placing the order'
        },
        {
            'name': 'title',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Product title'
        },
        {
            'name': 'brand',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Product brand'
        },
        {
            'name': 'description',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'Product description'
        },
        {
            'name': 'price',
            'in': 'formData',
            'type': 'float',
            'required': True,
            'description': 'Product price'
        },
        {
            'name': 'quantity',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'Quantity of product ordered'
        },
        {
            'name': 'img',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Product image'
        }
    ],
    'consumes': [
        'multipart/form-data',
    ],
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
                            'name': {
                                'type': 'string',
                                'example': 'John Doe'
                            },
                            'email': {
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
