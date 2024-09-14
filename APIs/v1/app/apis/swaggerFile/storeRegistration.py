# Swagger documentation for the Store API endpoints

# Documentation for creating a store endpoint
createStoreDoc = {
    'tags': ['Store Management'],
    'parameters': [
        {
            'name': 'store_name',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'The name of the store'
        },
        {
            'name': 'store_location',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'The physical location of the store'
        },
        {
            'name': 'store_email',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'The email address of the store'
        },
        {
            'name': 'store_phone_number',
            'in': 'formData',
            'type': 'string',
            'required': True,
            'description': 'The phone number of the store'
        },
        {
            'name': 'operation_times',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Operating times of the store (e.g., 9am - 5pm)'
        },
        {
            'name': 'social_media_accounts',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Comma-separated social media accounts (optional)'
        },
        {
            'name': 'store_bio',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'A brief bio or description of the store'
        },
        {
            'name': 'inner_image',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Optional image showing the store interior'
        },
        {
            'name': 'outer_image',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Optional image showing the store exterior'
        }
    ],
    'consumes': [
        'multipart/form-data',  # Accepts file upload format for images
    ],
    'responses': {
        201: {
            'description': 'Store created successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Store successfully created!'
                    },
                    'data': {
                        'type': 'object',
                        'properties': {
                            'store_id': {
                                'type': 'integer',
                                'example': 1
                            },
                            'store_name': {
                                'type': 'string',
                                'example': 'Tech Store'
                            },
                            'store_location': {
                                'type': 'string',
                                'example': '123 Main St, City, Country'
                            },
                            'store_email': {
                                'type': 'string',
                                'example': 'store@example.com'
                            },
                            'store_phone_number': {
                                'type': 'string',
                                'example': '+1234567890'
                            },
                            'operation_times': {
                                'type': 'string',
                                'example': '9 AM - 5 PM'
                            },
                            'social_media_accounts': {
                                'type': 'string',
                                'example': 'facebook.com/techstore, twitter.com/techstore'
                            },
                            'store_bio': {
                                'type': 'string',
                                'example': 'We sell the latest tech gadgets.'
                            },
                            'inner_image_url': {
                                'type': 'string',
                                'example': '/static/store_images/inner.jpg'
                            },
                            'outer_image_url': {
                                'type': 'string',
                                'example': '/static/store_images/outer.jpg'
                            },
                            'created_at': {
                                'type': 'string',
                                'example': '2023-09-14T12:00:00Z'
                            },
                            'updated_at': {
                                'type': 'string',
                                'example': '2023-09-14T12:00:00Z'
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
        409: {
            'description': 'Store already exists',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Store already exists'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while creating the store',
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

# Documentation for updating a store endpoint
updateStoreDoc = {
    'tags': ['Store Management'],
    'parameters': [
        {
            'name': 'store_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the store to be updated'
        },
        {
            'name': 'store_name',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Updated name of the store'
        },
        {
            'name': 'store_location',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Updated location of the store'
        },
        {
            'name': 'store_email',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Updated email of the store'
        },
        {
            'name': 'store_phone_number',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Updated phone number of the store'
        },
        {
            'name': 'operation_times',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Updated operating times of the store (e.g., 9am - 5pm)'
        },
        {
            'name': 'social_media_accounts',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Updated comma-separated social media accounts (optional)'
        },
        {
            'name': 'store_bio',
            'in': 'formData',
            'type': 'string',
            'required': False,
            'description': 'Updated brief bio or description of the store'
        },
        {
            'name': 'inner_image',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Optional updated image showing the store interior'
        },
        {
            'name': 'outer_image',
            'in': 'formData',
            'type': 'file',
            'required': False,
            'description': 'Optional updated image showing the store exterior'
        }
    ],
    'consumes': [
        'multipart/form-data',  # Accepts file upload format for images
    ],
    'responses': {
        200: {
            'description': 'Store updated successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Store updated successfully!'
                    }
                }
            }
        },
        404: {
            'description': 'Store not found or unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Store not found or unauthorized access'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while updating the store',
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

# Documentation for deleting a store endpoint
deleteStoreDoc = {
    'tags': ['Store Management'],
    'parameters': [
        {
            'name': 'store_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the store to be deleted'
        }
    ],
    'responses': {
        200: {
            'description': 'Store deleted successfully',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'success'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Store deleted successfully!'
                    }
                }
            }
        },
        404: {
            'description': 'Store not found or unauthorized access',
            'schema': {
                'type': 'object',
                'properties': {
                    'status': {
                        'type': 'string',
                        'example': 'error'
                    },
                    'message': {
                        'type': 'string',
                        'example': 'Store not found or unauthorized access'
                    }
                }
            }
        },
        500: {
            'description': 'An error occurred while deleting the store',
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
