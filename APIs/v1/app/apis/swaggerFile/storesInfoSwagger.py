
"""Swagger documentation for the Store API endpoints"""

getStoresDoc = {
    "tags": ["Store account Management"],
    "summary": "Retrieve all stores",
    "description": "Fetches all stores from the database along with their details.",
    "responses": {
    "200": {
        "description": "Successfully retrieved all stores",
        "schema": {
        "type": "object",
        "properties": {
            "status": {
            "type": "string",
            "example": "success"
            },
            "message": {
            "type": "string",
            "example": "Stores successfully retrieved"
            },
            "stores": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                "id": {
                    "type": "integer",
                    "example": 1
                },
                "owner": {
                    "type": "string",
                    "example": "John Doe"
                },
                "phoneNumber": {
                    "type": "string",
                    "example": "+1234567890"
                },
                "email": {
                    "type": "string",
                    "example": "store@example.com"
                },
                "storeName": {
                    "type": "string",
                    "example": "Tech Store"
                },
                "outer_image": {
                    "type": "string",
                    "example": "/static/store_images/outer.jpg"
                },
                "inner_image": {
                    "type": "string",
                    "example": "/static/store_images/inner.jpg"
                }
                }
            }
            }
        }
        }
    },
    "404": {
        "description": "No stores found",
        "schema": {
        "type": "object",
        "properties": {
            "status": {
            "type": "string",
            "example": "error"
            },
            "message": {
            "type": "string",
            "example": "No stores found"
            }
        }
        }
    },
    "500": {
        "description": "Internal Server Error",
        "schema": {
        "type": "object",
        "properties": {
            "status": {
            "type": "string",
            "example": "error"
            },
            "message": {
            "type": "string",
            "example": "Internal Server Error"
            }
        }
        }
    }
    }
}
