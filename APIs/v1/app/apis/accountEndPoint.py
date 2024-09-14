#!/usr/bin/python3
""" Account mangment Endpoints """
from flask import request, jsonify
from flassger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import account
from .swaggerFile import accountDoc
from ..models import User, Provider
from .. import db
from .. import limiter


@account.route('/account', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(accountDoc)
def getAccount():
    """Get the user's account"""
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
        user = Provider.query.filter_by(email=currentUserEmail).first()
        return jsonify({
                "status": "error",
                "message": "User not found"
                }), 404
    # Return success response
    return jsonify({
            "status": "success",
            "data": {
                    "userId": user.id,
                    "first name": user.first_name,
                    "last name": user.last_name,
                    "username": user.username,
                    "email": user.email,
                    "phone number": user.phone_number,
                    "gander": user.gander,
                    "location": user.location,
                    "profile image": user.profile_image,
                }
            }), 200
