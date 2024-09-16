#!/usr/bin/python3
""" Products mangment Endpoints """
from flask import request, jsonify
from flasgger import swag_from # type: ignore
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from . import product
# from .swaggerFile import productDoc, productUpdateDoc
from ..models import Product, Provider
from ..utils import saveProfilePicture
from .. import db
from .. import limiter


@product.route('/add-product', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
# @swag_from(accountDoc)
def addProduct():
    """Add products to the provider store account"""
    # Get the profivder's email from the token
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
            }), 400
    # Get the provider
    user = Provider.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
                "status": "error",
                "message": "User not found"
                }), 404

    # Check the request data
    if not request.form:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
            }), 400

    # Get the store id 
    storeId = request.form.get('store_id')
    name = request.form.get('name')
    brand = request.form.get('brand')
    category = request.form.get('category')
    description = request.form.get('description')
    price = request.form.get('price')
    deliveryStatus = request.form.get('status')
    image_1 = request.form.get('image_1')
    image_2 = request.form.get('image_2')
    image_3 = request.form.get('image_3')
    image_4 = request.form.get('image_4')

    # Create new product
    newProduct = Product(storeId=storeId, name=name, brand=brand,
                         category=category, description=description,
                         price=price, deliveryStatus=deliveryStatus,
                         image_1=image_1, image_2=image_2, image_3=image_3,
                         image_4=image_4
                         )
    # Save the user updates
    db.session.commit()
    # Return success response
    return jsonify({
            "status": "success",
            "message": "Product added successfully",
            "data" : newProduct.to_dict()
            }), 200
