"""Swagger documentation for the getAllProductsByCategory endpoint"""

getAllProductsByCategoryDoc = {
    'tags': ['Store account Management'],
    'summary': 'Retrieve all products grouped by category',
    'description': 'Fetches all distinct product categories and returns products for each category.',
    'responses': {
        200: {
            'description': 'Products successfully retrieved',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Products successfully retrieved'
                    },
                    'categories': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'category_name': {
                                    'type': 'string',
                                    'example': 'Electronics'
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
                                            'name': {
                                                'type': 'string',
                                                'example': 'Smartphone'
                                            },
                                            'brand': {
                                                'type': 'string',
                                                'example': 'TechBrand'
                                            },
                                            'description': {
                                                'type': 'string',
                                                'example': 'Latest model with advanced features'
                                            },
                                            'price': {
                                                'type': 'number',
                                                'format': 'float',
                                                'example': 299.99
                                            },
                                            'image_url': {
                                                'type': 'string',
                                                'example': '/static/product_images/smartphone.jpg'
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
            'description': 'No categories found',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'No categories found'
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
                        'example': 'An error occurred while retrieving products'
                    }
                }
            }
        }
    }
}
