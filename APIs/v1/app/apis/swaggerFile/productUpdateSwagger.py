"""Swagger documentation for product update endpoints"""
# product.py

# Documentation for the product update endpoint
productUpdateDoc = {
    'tags': ['Update product in the provider store'],     
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': False,
            'type': 'string',
            'description': 'Bearer token' 
        }
        ,
        {
            'name': 'storeId',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'name',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'brand',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'category',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'description',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'price',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'deliveryStatus',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'location',
            'in': 'formData',
            'type': 'string',
            'required': False
        }
        ,
        {
            'name': 'image_1',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Product image'
        }
        ,
        {
            'name': 'image_2',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Product image'
        }
        ,
        {
            'name': 'image_3',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'OProduct image'
        }
         ,
        {
            'name': 'image_4',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Product image'
        }
    ],
    'consumes': [
        'multipart/form-data',  # Set the content type to JSON
    ],
    'responses': {
        200: {
            'description': 'User account.',
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
                            'brand name': {
                                'type': 'string',
                                'example': 'AKJ'
                            },
                            'category': {
                                'type': 'string',
                                'example': 'Power'
                            },
                            'description': {
                                'type': 'string',
                                'example': 'High power powerbanck',
                            },
                            'price': {
                                'type': 'string',
                                'example': '125.600'
                            },
                            'gander': {
                                'type': 'string',
                                'example': 'male'
                            },
                            'deliveryStatus': {
                                'type': 'string',
                                'example': 'False/False'
                            },
                            'image_1': {
                                'type': 'string',
                                'example': 'image_1.png'
                            }
                            ,
                            'image_2': {
                                'type': 'string',
                                'example': 'image_2.png'
                            }
                            ,
                            'image_3': {
                                'type': 'string',
                                'example': 'image_3.png'
                            }
                            ,
                            'image_4': {
                                'type': 'string',
                                'example': 'image_4.png'
                            }
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Bad request, no user token.',
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
                        'example': 'Bad request.'
                    }
                }
            }
        }
    }
}
