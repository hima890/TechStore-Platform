searchProductDoc = {
    'tags': ['Products'],
    'description': 'Search products by category and store name. You can search by either or both.',
    'parameters': [
        {
            'name': 'category',
            'in': 'query',
            'type': 'string',
            'description': 'The category of the products to search for.',
            'required': False
        },
        {
            'name': 'store_name',
            'in': 'query',
            'type': 'string',
            'description': 'The store name to search for products in.',
            'required': False
        }
    ],
    'responses': {
        '200': {
            'description': 'Products found successfully',
            'examples': {
                'application/json': {
                    'status': 'success',
                    'message': 'Products found',
                    'data': [
                        {
                            'id': 1,
                            'name': 'Laptop',
                            'brand': 'BrandName',
                            'category': 'Electronics',
                            'price': 999.99,
                            'description': 'High-end laptop with great features',
                            'store_name': 'BestStore',
                            'image_1': 'image_url'
                        }
                    ]
                }
            }
        },
        '404': {
            'description': 'No products found',
            'examples': {
                'application/json': {
                    'status': 'error',
                    'message': 'No products found for the provided criteria'
                }
            }
        },
        '400': {
            'description': 'Bad request, missing search parameters',
            'examples': {
                'application/json': {
                    'status': 'error',
                    'message': 'Please provide either a category or store name to search'
                }
            }
        }
    }
}
