# Swagger documentation for the Orders API endpoints

# Documentation for getting all orders
getAllOrdersDoc = {
    'tags': ['Order Management'],
    'parameters': [
        {
            'name': 'Authorization',
            'in': 'header',
            'required': True,
            'type': 'string',
            'description': 'Bearer token'
        }
    ],
    'responses': {
        200: {
            'description': 'List of all orders retrieved successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'data': {
                        'type': 'array',
                        'items': {
                            'type': 'object',
                            'properties': {
                                'id': {
                                    'type': 'integer',
                                    'example': 1
                                },
                                'user_id': {
                                    'type': 'integer',
                                    'example': 1
                                },
                                'store_id': {
                                    'type': 'integer',
                                    'example': 1
                                },
                                'product_id': {
                                    'type': 'integer',
                                    'example': 1
                                },
                                'order_date': {
                                    'type': 'string',
                                    'example': '2023-09-14T12:00:00Z'
                                },
                                'quantity': {
                                    'type': 'integer',
                                    'example': 2
                                },
                                'total_price': {
                                    'type': 'float',
                                    'example': 100.00
                                }
                            }
                        }
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized - Invalid or missing token',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Unauthorized access'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while retrieving the orders',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Internal Server Error'
                    }
                }
            }
        }
    }
}

# Documentation for getting a single order by ID
getOrderDoc = {
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
            'name': 'order_id',
            'in': 'path',
            'required': True,
            'type': 'integer',
            'description': 'ID of the order to retrieve'
        }
    ],
    'responses': {
        200: {
            'description': 'Order retrieved successfully',
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
                            'id': {
                                'type': 'integer',
                                'example': 1
                            },
                            'user_id': {
                                'type': 'integer',
                                'example': 1
                            },
                            'store_id': {
                                'type': 'integer',
                                'example': 1
                            },
                            'product_id': {
                                'type': 'integer',
                                'example': 1
                            },
                            'order_date': {
                                'type': 'string',
                                'example': '2023-09-14T12:00:00Z'
                            },
                            'quantity': {
                                'type': 'integer',
                                'example': 2
                            },
                            'total_price': {
                                'type': 'float',
                                'example': 100.00
                            }
                        }
                    }
                }
            }
        },
        404: {
            'description': 'Order not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Order not found'
                    }
                }
            }
        },
        401: {
            'description': 'Unauthorized - Invalid or missing token',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Unauthorized access'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while retrieving the order',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Internal Server Error'
                    }
                }
            }
        }
    }
}