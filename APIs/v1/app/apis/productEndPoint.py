#!/usr/bin/python3
""" Product Management Endpoints """
from flask import request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import product
from ..models import Store
from .swaggerFile import productDoc, productUpdateDoc, productDeleteDoc, getAllProductsByCategoryDoc, searchProductDoc
from ..models import Product, Provider
from ..utils import saveProductImagesFunc
from ..utils import updateProductImageFunc
from ..utils import deleteProductImageFunc
from ..utils import generateProductIdFunc
from .. import db
from .. import limiter


@product.route('/add-product', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(productDoc)
def addProduct():
    """Add products to the provider store account"""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400

    user = Provider.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    if not request.form:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
        }), 400

    storeId = request.form.get('store_id')
    name = request.form.get('name')
    brand = request.form.get('brand')
    category = request.form.get('category')
    description = request.form.get('description')
    price = request.form.get('price')
    deliveryStatus = request.form.get('status')
    image_1 = request.files.get('image_1')

    # Convert deliveryStatus to boolean
    if deliveryStatus in ['true', 'True', 'on', '1']:  # Treat 'true', 'on', '1' as True
        deliveryStatus = True
    else:
        deliveryStatus = False  # Treat other values (or if not set) as False

    # Save product image
    newFileName, newFilePath = saveProductImagesFunc([image_1])

    # Generate a unique product ID
    newId = generateProductIdFunc()

    # Create a new Product instance
    newProduct = Product(
        store_id=storeId,
        name=name,
        product_id=newId,
        brand=brand,
        category=category,
        description=description,
        price=price,
        deliveryStatus=deliveryStatus,
        image_1=newFileName[0]
    )

    # Add and commit new product to the database
    db.session.add(newProduct)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product added successfully",
        "data": newProduct.to_dict()
    }), 200


@product.route('/update-product', methods=['PUT'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(productUpdateDoc)
def updateProduct():
    """Update product details"""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400

    user = Provider.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    if not request.form:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
        }), 400

    productID = request.form.get('product_id')
    product = Product.query.filter_by(id=productID).first()

    if not product:
        product = Product.query.filter_by(product_id=productID).first()
        if not product:
            return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404
       

    # Update product fields
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
        # Convert deliveryStatus to boolean
        deliveryStatus = request.form.get('status')
        if deliveryStatus in ['true', 'True', 'on', '1']:  # Treat 'true', 'on', '1' as True
            product.deliveryStatus = True
        else:
            product.deliveryStatus = False  # Treat other values (or if not set) as False

    # Update product image if provided
    if request.files.get('image_1'):
        unique_filename_1, _ = updateProductImageFunc(request.files.get('image_1'))
        product.image_1 = unique_filename_1

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Product updated successfully",
        "data": product.to_dict()
    }), 200


@product.route('/delete-product', methods=['DELETE'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(productDeleteDoc)
def deleteProduct():
    """Delete a product and its image."""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400

    user = Provider.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    productID = request.form.get('product_id')
    product = Product.query.filter_by(product_id=productID).first()

    if not product:
        return jsonify({
            "status": "error",
            "message": "Product not found"
        }), 404

    # Delete product image
    if product.image_1:
        deleteProductImageFunc(product.image_1)

    try:
        db.session.delete(product)
        db.session.commit()
        return jsonify({
            "status": "success",
            "message": "Product deleted successfully"
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({
            "status": "error",
            "message": "Error deleting product from database: {}".format(e)
        }), 500


@product.route('/get-products', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(getAllProductsByCategoryDoc)
def getAllProducts():
    """Get all the products under every category"""
    categories = db.session.query(Product.category).distinct().all()

    if not categories:
        return jsonify({
            'status': 'error',
            'message': 'No categories found'
        }), 404

    categoryList = []
    for category_tuple in categories:
        category_name = category_tuple[0]
        categoryData = {
            'category_name': category_name,
            'products': []
        }

        products = Product.query.filter_by(category=category_name).all()
        for product in products:
            productData = product.to_dict()
            categoryData['products'].append(productData)
        categoryList.append(categoryData)

    return jsonify({
        'status': 'success',
        'message': 'Products successfully retrieved',
        'categories': categoryList
    }), 200


@product.route('/search-products', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(searchProductDoc)
def searchProducts():
    """Search products by category and store name"""
    category = request.args.get('category')
    store_name = request.args.get('store_name')

    if not category and not store_name:
        products = Product.query.all()  # Get all products if no filter is applied
    else:
        query = Product.query
        if category:
            query = query.filter_by(category=category)
        if store_name:
            query = query.join(Store).filter(Store.store_name.ilike(f'%{store_name}%'))
        products = query.all()

    if not products:
        return jsonify({
            'status': 'error',
            'message': 'No products found for the provided criteria'
        }), 404

    productList = []
    for product in products:
        data = product.to_dict()
        productList.append(data)

    return jsonify({
        'status': 'success',
        'message': 'Products found',
        'data': productList
    }), 200
