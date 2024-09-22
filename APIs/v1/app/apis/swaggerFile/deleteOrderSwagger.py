deleteOrderDoc = {
    'tags': ['Order Management'],
    'summary': 'Delete an order',
    'description': 'Delete a specific order by its order_id',
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
                    'order_id': {
                        'type': 'integer',
                        'description': 'ID of the order to be deleted',
                        'example': 1
                    }
                }
            }
        }
    ],
    'consumes': ['application/json'],
    'responses': {
        200: {
            'description': 'Order deleted successfully.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Order deleted successfully.'
                    }
                }
            }
        },
        404: {
            'description': 'Order not found.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Order not found.'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while deleting the order.',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Internal Server Error.'
                    }
                }
            }
        }
    }
}
