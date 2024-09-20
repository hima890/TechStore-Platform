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
    """Orders end point"""
    # Get the user's email from the token
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

    # Check the request data
    if not request.form:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
            }), 400

    # Get the order data
    name = request.form.get('name')
    email = request.form.get('email')
    store_id = request.form.get('store_id')
    title = request.form.get('title')
    brand = request.form.get('brand')
    orderImage = request.files.get('img')
    description = request.form.get('description')
    price = float(request.form.get('price'))
    quantity = int(request.form.get('quantity'))
    total = price * quantity

    # Check if the store exists
    store = Store.query.get(store_id)
    if not store:
        return jsonify({
            "status": "error",
            "message": "Store not found"
            }), 404

    # Validate and process the profile picture
    if orderImage:
        filename, _ = saveOrdersPicture(orderImage)
    else:
        filename = None  # Handle cases where no picture is uploaded
        
    newOrder = Order(
        name=name,
        email=email,
        store_id=store_id,
        title=title,
        brand=brand,
        description=description,
        price=price,
        img=filename,
        quantity=quantity,
        total=total
    )

    # Save the order to the database
    db.session.add(newOrder)
    db.session.commit()

    # Return the order details
    return jsonify({
            "status": "success",
            "message": "Order created successfully!",
            "data": {
                newOrder.to_dict()
            }
        }), 201


@orders.route('/get-order', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(getStoreOrdersDoc)
def getOrder():
    """Get the store orders"""
    # Get the user's email from the token
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

    # Check the request data
    if not request.form:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
            }), 400

    # Get the store id
    store_id = request.form.get('store_id')
    store = Store.query.get(store_id)
    if not store:
        return jsonify({
            "status": "error",
            "message": "Store not found"
            }), 404

    # Get the store orders
    orders = Order.query.filter_by(store_id=store_id).all()
    if not orders:
        return jsonify({
            "status": "success",
            "message": "No orders found for this store"
            }), 200

    # Return the store orders
    orderList = []
    for order in orders:
        orderList.append({
            "order_id": order.id,
            "name": order.name,
            "email": order.email,
            "store_id": order.store_id,
            "title": order.title,
            "brand": order.brand,
            "description": order.description,
            "price": order.price,
            "quantity": order.quantity,
            "total": order.total,
            "img": order.img
        })

    return jsonify({
        "status": "success",
        "message": "Orders found",
        "data": orderList
    }), 200


@orders.route('/delete-order', methods=['DELETE'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(deleteOrderDoc)  # Use the Swagger doc for deleting orders
def deleteOrder():
    """Delete an order"""
    # Get the user's email from the token
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

    # Get the request data for the order ID
    order_id = request.form.get('order_id')
    if not order_id:
        return jsonify({
            "status": "error",
            "message": "Order ID is required"
        }), 400

    # Get the order by ID
    order = Order.query.get(order_id)
    if not order:
        return jsonify({
            "status": "error",
            "message": "Order not found"
        }), 404

    # Delete the order
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
