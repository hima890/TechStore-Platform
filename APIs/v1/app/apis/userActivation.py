#!/usr/bin/python3
""" Activation API Endpoints """
from .swaggerFile.activation import activation
from flask import request, jsonify, url_for
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from . import activation
from .. import db
from ..models.user import User
from ..models.provider import Provider



@activation.route('/activate', methods=['GET'])
@jwt_required(optional=True)
@swag_from(activation)
def activate_account():
    """Get the token from the URL and activate the user account"""
    # Get the token from the URL
    current_user = get_jwt_identity()
    # Check it the token blong to a user
    if not current_user:
        # Return an error message if the token is invalid or expired
        return jsonify(
            {"error": "Invalid or expired token"}
            ), 400
    # Filter the User table by email and check if the user exists
    user = User.query.filter_by(email=current_user).first()
    # Check if the user exists
    if not user:
        user = Provider.query.filter_by(email=current_user).first()
        if not user:
            # Return an error message if the user does not exist
            return jsonify(
                {"msg": "User not found"}
                ), 404
    # If the user exists, activate the account
    user.is_active = True
    # Save the changes to the database
    db.session.commit()
    # Return a success message with a 200 status code
    return jsonify(
        {"status": "success",},
        {"message": "Account activated successfully"}
        ), 200
