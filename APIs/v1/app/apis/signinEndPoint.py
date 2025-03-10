#!/usr/bin/python3
""" Signin API Endpoints """
from flasgger import swag_from
from flask import request, jsonify
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from . import signIn
from .swaggerFile import siginDoc
from .. import limiter
from ..models import User, Provider


@signIn.route('/signin', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(siginDoc)
def signin():
    """Sign in a user"""
    if request.content_type == 'application/json':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user:
        user = Provider.query.filter_by(email=email).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
                }), 404

    if user.is_active != True:
        return jsonify({
                "status": "error",
                "message": "User acount need to be activated"
                }), 401

    if not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid password"}), 401

    try:
        access_token = create_access_token(
            identity=user.email,
            expires_delta=timedelta(hours=24))

        return jsonify({
            "status": "success",
            "message": "Authentication successful",
            "data": {
                "email": user.email,
                "username": user.username,
                "userId": user.id,
                "token": access_token,
                'account_type': user.account_type,
                'phone_number': user.phone_number
            }
        }), 200

    except Exception as e:
        print("{}".format(e))
        return jsonify({
            "status": "error",
            "message": "An error occurred while authenicate the user."
            }), 500
