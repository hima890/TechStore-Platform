# Swagger documentation for the Orders API endpoints

# Documentation for creating an order endpoint
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
            'name': 'user_id',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the user placing the order'
        },
        {
            'name': 'store_id',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the store from which the order is being placed'
        },
        {
            'name': 'product_id',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'The ID of the product being ordered'
        },
        {
            'name': 'quantity',
            'in': 'formData',
            'type': 'integer',
            'required': True,
            'description': 'The quantity of the product being ordered'
        },
        {
            'name': 'total_price',
            'in': 'formData',
            'type': 'float',
            'required': True,
            'description': 'The total price of the order'
        }
    ],
    'responses': {
        201: {
            'description': 'Order created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Order successfully created!'
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
                                'example': 123
                            },
                            'store_id': {
                                'type': 'integer',
                                'example': 456
                            },
                            'product_id': {
                                'type': 'integer',
                                'example': 789
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
                                'example': 49.99
                            }
                        }
                    }
                }
            }
        },
        400: {
            'description': 'Missing or invalid fields',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Missing required fields'
                    }
                }
            }
        },
        404: {
            'description': 'Product, User, or Store not found',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Product, User, or Store not found'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while creating the order',
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

# Documentation for updating an order endpoint
updateOrderDoc = {
    'tags': ['Order Management'],
    'parameters': [
        {
            'name': 'order_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the order to be updated'
        },
        {
            'name': 'quantity',
            'in': 'formData',
            'type': 'integer',
            'required': False,
            'description': 'Updated quantity of the product in the order'
        },
        {
            'name': 'total_price',
            'in': 'formData',
            'type': 'float',
            'required': False,
            'description': 'Updated total price of the order'
        }
    ],
    'responses': {
        200: {
            'description': 'Order updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Order updated successfully!'
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
        500: {
            'description': 'An error occurred while updating the order',
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

# Documentation for deleting an order endpoint
deleteOrderDoc = {
    'tags': ['Order Management'],
    'parameters': [
        {
            'name': 'order_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the order to be deleted'
        }
    ],
    'responses': {
        200: {
            'description': 'Order deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Order deleted successfully!'
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
        500: {
            'description': 'An error occurred while deleting the order',
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
