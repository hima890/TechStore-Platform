#!/usr/bin/python3
""" Signin API Endpoints """
from flasgger import swag_from
from .. import limiter
from flask import request, jsonify
from datetime import timedelta
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token
from ..models.user import User
from ..models.provider import Provider
from .swaggerFile.loginSwagger import login
from . import signIn



@signIn.route('/signin', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(login)
def signin():
    """Sign in a user"""
    # Get the request data based on the content_type
    if request.content_type == 'application/json':
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if not user:
        user = Provider.query.filter_by(email=email).first()
        if not user:
            return jsonify({"error": "User not found"}), 404

    # Check if the password is correct
    if not check_password_hash(user.password_hash, password):
        return jsonify({"error": "Invalid password"}), 401

    # Return a success message and a token for subrequests
    # Generate JWT token whit the user email as the identity and for 24 hours
    try:
        access_token = create_access_token(
            identity=user.email,
            expires_delta=timedelta(hours=24))
        # return the a response with access token
        return jsonify({
            "status": "success",
            "message": "Authentication successful",
            "data": {
                "email": user.email,
                "username": user.username,
                "userId": user.id,
                "token": access_token
            }
        }), 200

    except Exception as e:
        # Return to the last change
        print("{}".format(e))
        return jsonify({"error": "An error occurred while authenicate the user."}), 500
