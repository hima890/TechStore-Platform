#!/usr/bin/python3
""" Orders API Endpoints """
from flask import request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flasgger import swag_from
from . import orders
from .swaggerFile import createOrderDoc, getStoreOrdersDoc, deleteOrderDoc
from ..models import User, Store, Order
from .. import db
from .. import limiter
from ..utils import saveOrdersPicture


@orders.route('/add-order', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(createOrderDoc)
def addOrders():
    """Create an order"""
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

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
        }), 400

    # Get request data
    requester_name = data.get('requester_name')
    requester_email = data.get('requester_email')
    store_id = data.get('store_id')
    title = data.get('title')
    brand = data.get('brand')
    description = data.get('description')
    price = float(data.get('price'))
    quantity = int(data.get('quantity'))
    total = price * quantity
    orderImage = request.files.get('img')

    # Check store existence
    store = Store.query.get(store_id)
    if not store:
        return jsonify({
            "status": "error",
            "message": "Store not found"
        }), 404

    # Save order image if provided
    filename = None
    if orderImage:
        filename, _ = saveOrdersPicture(orderImage)

    # Create and save new order
    newOrder = Order(
        requester_name=requester_name,
        requester_email=requester_email,
        store_id=store_id,
        title=title,
        brand=brand,
        description=description,
        price=price,
        img=filename,
        quantity=quantity,
        total=total,
        user_id=user.id  # link order to user
    )

    db.session.add(newOrder)
    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "Order created successfully!",
        "data": newOrder.to_dict()
    }), 201


@orders.route('/get-order', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(getStoreOrdersDoc)
def getOrder():
    """Get orders for the store or user"""
    currentUserEmail = get_jwt_identity()

    current_user = User.query.filter_by(email=currentUserEmail).first()
    if not current_user:
        return jsonify({
            "status": "error",
            "message": "User not found"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
        }), 400

    store_id = data.get('store_id')

    store = Store.query.get(store_id)
    if not store:
        return jsonify({
            "status": "error",
            "message": "Store not found"
        }), 404

    # Check if the user is either the provider or the customer who placed the order
    if current_user.id == store.provider_id or current_user.id == store.user_id:
        orders = Order.query.filter_by(store_id=store_id).all()

        if not orders:
            return jsonify({
                "status": "success",
                "message": "No orders found for this store"
            }), 200

        orderList = [order.to_dict() for order in orders]

        return jsonify({
            "status": "success",
            "message": "Orders found",
            "data": orderList
        }), 200

    return jsonify({
        "status": "error",
        "message": "You do not have permission to view these orders"
    }), 403


@orders.route('/delete-order', methods=['DELETE'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(deleteOrderDoc)
def deleteOrder():
    """Delete an order"""
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

    data = request.get_json()
    order_id = data.get('order_id')
    if not order_id:
        return jsonify({
            "status": "error",
            "message": "Order ID is required"
        }), 400

    order = Order.query.get(order_id)
    if not order:
        return jsonify({
            "status": "error",
            "message": "Order not found"
        }), 404

    # Check if the user has permission to delete this order
    if user.id == order.user_id or user.id == order.store.provider_id:
        try:
            db.session.delete(order)
            db.session.commit()
            return jsonify({
                "status": "success",
                "message": "Order deleted successfully"
            }), 200
        except Exception as e:
            db.session.rollback()
            return jsonify({
                "status": "error",
                "message": "An error occurred while deleting the order"
            }), 500

    return jsonify({
        "status": "error",
        "message": "You do not have permission to delete this order"
    }), 403
