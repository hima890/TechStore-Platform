
"""Swagger documentation for the GET /stores endpoint""" 


getAllStoresDoc = {
    'tags': ['Store Management'],
    'summary': 'Retrieve all stores with their associated products',
    'description': 'This endpoint retrieves a list of all stores in the database, including the products associated with each store.',
    'responses': {
        200: {
            'description': 'Successfully retrieved all stores and their products',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'All stores in the database'
                    },
                    'stores': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'store_id': {
                                    'type': 'integer',
                                    'example': 1
                                },
                                'provider_id': {
                                    'type': 'integer',
                                    'example': 101
                                },
                                'store_name': {
                                    'type': 'string',
                                    'example': 'Tech Gadgets'
                                },
                                'store_location': {
                                    'type': 'string',
                                    'example': 'New York, NY'
                                },
                                'store_email': {
                                    'type': 'string',
                                    'example': 'info@techgadgets.com'
                                },
                                'store_phone_number': {
                                    'type': 'string',
                                    'example': '+1234567890'
                                },
                                'operation_times': {
                                    'type': 'string',
                                    'example': 'Mon-Fri 9am-6pm'
                                },
                                'social_media_accounts': {
                                    'type': 'string',
                                    'example': 'twitter.com/techgadgets'
                                },
                                'store_bio': {
                                    'type': 'string',
                                    'example': 'Leading provider of tech gadgets'
                                },
                                'inner_image_url': {
                                    'type': 'string',
                                    'example': 'https://example.com/static/store_images/inner_image1.jpg'
                                },
                                'outer_image_url': {
                                    'type': 'string',
                                    'example': 'https://example.com/static/store_images/outer_image1.jpg'
                                },
                                'created_at': {
                                    'type': 'string',
                                    'example': '2024-09-16T12:00:00'
                                },
                                'updated_at': {
                                    'type': 'string',
                                    'example': '2024-09-16T12:00:00'
                                },
                                'products': {
                                    'type': 'array',
                                    'items': {
                                        'type': 'object',
                                        'properties': {
                                            'id': {
                                                'type': 'integer',
                                                'example': 1
                                            },
                                            'store_id': {
                                                'type': 'integer',
                                                'example': 1
                                            },
                                            'name': {
                                                'type': 'string',
                                                'example': 'Smartphone XYZ'
                                            },
                                            'brand': {
                                                'type': 'string',
                                                'example': 'XYZ'
                                            },
                                            'category': {
                                                'type': 'string',
                                                'example': 'Mobile'
                                            },
                                            'description': {
                                                'type': 'string',
                                                'example': 'Latest smartphone with amazing features'
                                            },
                                            'price': {
                                                'type': 'number',
                                                'format': 'float',
                                                'example': 799.99
                                            },
                                            'deliveryStatus': {
                                                'type': 'boolean',
                                                'example': true
                                            },
                                            'image_1': {
                                                'type': 'string',
                                                'example': 'https://example.com/static/product_images/smartphone1_image1.jpg'
                                            },
                                            'image_2': {
                                                'type': 'string',
                                                'example': 'https://example.com/static/product_images/smartphone1_image2.jpg'
                                            },
                                            'image_3': {
                                                'type': 'string',
                                                'example': 'https://example.com/static/product_images/smartphone1_image3.jpg'
                                            },
                                            'image_4': {
                                                'type': 'string',
                                                'example': 'https://example.com/static/product_images/smartphone1_image4.jpg'
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'No stores found',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'No stores found'
                    }
                }
            }
        },
        500: {
            'description': 'Internal Server Error',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'An error occurred while retrieving stores'
                    }
                }
            }
        }
    },
    'security': [
        {
            'BearerAuth': []
        }
    ]
}
