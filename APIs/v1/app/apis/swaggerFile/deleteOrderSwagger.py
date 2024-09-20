# Swagger documentation for the delete order endpoint
deleteOrderDoc = {
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
            'type': 'integer',
            'required': True,
            'description': 'ID of the order to be deleted'
        }
    ],
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
