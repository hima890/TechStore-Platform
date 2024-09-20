#!/usr/bin/python3
""" Orders Management Endpoints """
from flask import request, jsonify
from flasgger import swag_from  # type: ignore
from flask_jwt_extended import jwt_required, get_jwt_identity  # type: ignore
from . import order
from .swaggerFile import orderCreateDoc, orderDeleteDoc, getOrderDoc, getAllOrdersDoc
from ..models import Order, Product, Store, User
from .. import db
from .. import limiter


@order.route('/create-order', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(orderCreateDoc)
def createOrder():
    """Create a new order for a product"""
    # Get the user's email from the token
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400
    
    # Get the user
    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    # Get the request data
    data = request.get_json()
    product_id = data.get('product_id')
    store_id = data.get('store_id')
    quantity = data.get('quantity')

    # Validate required fields
    if not all([product_id, store_id, quantity]):
        return jsonify({
            "status": "error",
            "message": "Missing required fields"
        }), 400

    # Find the store, product and calculate total price
    store = Store.query.get(store_id)
    product = Product.query.get(product_id)

    if not store or not product:
        return jsonify({
            "status": "error",
            "message": "Store or product not found"
        }), 404

    total_price = product.price * int(quantity)

    # Create new order
    newOrder = Order(
        user_id=user.id,
        store_id=store.id,
        product_id=product.id,
        quantity=quantity,
        total_price=total_price
    )

    db.session.add(newOrder)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Order created successfully",
        "data": newOrder.to_dict()
    }), 201


@order.route('/delete-order/<int:order_id>', methods=['DELETE'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(orderDeleteDoc)
def deleteOrder(order_id):
    """Delete an existing order"""
    # Get the user's email from the token
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400

    # Get the user
    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    # Find the order by ID
    order = Order.query.get(order_id)
    if not order:
        return jsonify({
            "status": "error",
            "message": "Order not found"
        }), 404

    # Check if the user is authorized to delete this order
    if order.user_id != user.id:
        return jsonify({
            "status": "error",
            "message": "Unauthorized action"
        }), 403

    # Delete the order
    db.session.delete(order)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Order deleted successfully"
    }), 200


@order.route('/get-order/<int:order_id>', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(getOrderDoc)
def getOrder(order_id):
    """Get details of a specific order"""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400

    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    # Find the order by ID
    order = Order.query.get(order_id)
    if not order:
        return jsonify({
            "status": "error",
            "message": "Order not found"
        }), 404

    # Check if the user is authorized to view this order
    if order.user_id != user.id:
        return jsonify({
            "status": "error",
            "message": "Unauthorized action"
        }), 403

    return jsonify({
        "status": "success",
        "data": order.to_dict()
    }), 200


@order.route('/get-orders', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(getAllOrdersDoc)
def getAllOrders():
    """Get all orders made by the current user"""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400

    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    # Get all orders made by the user
    orders = Order.query.filter_by(user_id=user.id).all()

    if not orders:
        return jsonify({
            "status": "error",
            "message": "No orders found"
        }), 404

    ordersList = [order.to_dict() for order in orders]

    return jsonify({
        "status": "success",
        "data": ordersList
    }), 200
