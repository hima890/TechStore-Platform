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
            'type': 'string',
            'description': 'Bearer token' 
        }
        ,
        {
            'name': 'storeId',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'name',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'brand',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'category',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'description',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'price',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'deliveryStatus',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'location',
            'in': 'formData',
            'type': 'string',
            'required': True
        }
        ,
        {
            'name': 'image_1',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'Product image'
        }
        ,
        {
            'name': 'image_2',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'Product image'
        }
        ,
        {
            'name': 'image_3',
            'in': 'formData',
            'type': 'file',
            'required': True,
            'description': 'OProduct image'
        }
         ,
        {
            'name': 'image_4',
            'in': 'formData',
            'type': 'file',
            'required': True,
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
                                'example': 'True/False'
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
