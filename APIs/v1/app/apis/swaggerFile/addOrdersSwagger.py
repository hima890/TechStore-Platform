# Swagger documentation for the create order endpoint
createOrderDoc = {
    'tags': ['Order Management'],     
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
            'name': 'requester_name',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Name of the customer placing the order'
        },
        {
            'name': 'requester_email',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Email of the customer placing the order'
        },
        {
            'name': 'store_id',
            'in': 'formData',
            'schema': {
                'type': 'integer'
            },
            'required': True,
            'description': 'ID of the store processing the order'
        },
        {
            'name': 'title',
            'in': 'formData',
            'schema': {
                'type': 'string'
            },
            'required': True,
            'description': 'Product title'
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
                'type': 'float'
            },
            'required': True,
            'description': 'Product price'
        },
        {
            'name': 'quantity',
            'in': 'formData',
            'schema': {
                'type': 'integer'
            },
            'required': True,
            'description': 'Quantity of the product ordered'
        },
        {
            'name': 'img',
            'in': 'formData',
            'schema': {
                'type': 'file'
            },
            'required': False,
            'description': 'Optional image of the product'
        }
    ],
    'consumes': [
        'multipart/form-data'
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
