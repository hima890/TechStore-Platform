#!/usr/bin/python3
""" Products mangment Endpoints """
from flask import request, jsonify
from flasgger import swag_from # type: ignore
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from . import product
from .swaggerFile import productDoc
from ..models import Product, Provider
from ..utils import saveProductImages, updateProductImage
from .. import db
from .. import limiter


@product.route('/add-product', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(productDoc)
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

    # Validate and process the product pictures
    newFileNames, newFilePath = saveProductImages([image_1, image_2, image_3, image_4])

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



@product.route('/update-product', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
# @swag_from(productDoc)
def updateProduct():
    """Update product details"""
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
    
    # Get the product id
    productID = request.form.get('product_id')
    product = Product.query.filter_by(product_id=productID).first()
    # Check if the product exists
    if not product:
        return jsonify({
            "status": "error",
            "message": "Product not found"
            }), 404

    # Update the product details
    if request.form.get('name'):
        product.name = request.form.get('name')
    if request.form.get('brand'):
        product.brand = request.form.get('brand')
    if request.form.get('category'):
        product.category = request.form.get('category')
    if request.form.get('description'):
        product.description = request.form.get('description')
    if request.form.get('price'):
        product.price = request.form.get('price')
    if request.form.get('status'):
        product.deliveryStatus = request.form.get('status')
    if request.form.get('image_1'):
        unique_filename_1, _ = updateProductImage(request.form.get('image_1'))
        product.image_1 = unique_filename_1
    if request.form.get('image_2'):
        unique_filename_2, _ = updateProductImage(request.form.get('image_2'))
        product.image_2 = unique_filename_2
    if request.form.get('image_3'):
        unique_filename_3, _ =  updateProductImage(request.form.get('image_3'))
        product.image_3 = unique_filename_3
    if request.form.get('image_4'):
        unique_filename_4, _ = updateProductImage(request.form.get('image_4'))
        product.image_4 = unique_filename_4
        
    # Save the user updates
    db.session.commit()
    # Return success response
    return jsonify({
            "status": "success",
            "message": "Product updated successfully",
            "data" : product.to_dict()
            }), 200
