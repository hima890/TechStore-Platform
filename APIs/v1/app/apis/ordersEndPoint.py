#!/usr/bin/python3
""" Orders API Endpoints """
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from datetime import timedelta
from . import ordersEndPoint
from .swaggerFile import optCodeDoc, verifyDoc
from ..models import User, Store, Order
from .. import db
from .. import limiter
from ..utils import generate_otp, send_email, isOtpValid


@ordersEndPoint.route('/opt', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
# @swag_from(optCodeDoc)
def orders():
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
    