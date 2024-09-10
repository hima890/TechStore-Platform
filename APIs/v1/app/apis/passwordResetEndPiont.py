#!/usr/bin/python3
""" Password reset Endpoints """
from flask import request, jsonify
from flasgger import swag_from
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import passwordReset
from .swaggerFile import resetDoc
from ..models import User, Provider
from .. import db
from .. import limiter


@passwordReset.route('/password-reset', methods=['POST'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(resetDoc)
# @swag_from(optCodeDoc)
def reset():
    """Reset a user's password"""
    # Get the user's email from the token
    currentUserEmail = get_jwt_identity()  # Get the user's email from the token
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
            }), 400

    # Get the new password fron the reqeust
    data = request.get_json()
    newPassword = data.get('newPassword')
    if not newPassword:
        return jsonify({
            "status": "error",
            "message": "Bad request, no password found"
            }), 400
    # Get the user
    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        user = Provider.query.filter_by(email=currentUserEmail).first()
        return jsonify({
                "status": "error",
                "message": "User not found"
                }), 404
    # Hash and update the new password
    user.password_hash = generate_password_hash(newPassword)
    db.session.commit()
    # Return success respound
    return jsonify({
            "status": "success",
            "message": "Password reset successful",
            "data": {
                    "email": user.email,
                    "username": user.username,
                    "userId": user.id
                }
            }), 200
