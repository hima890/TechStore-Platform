#!/usr/bin/python3
""" Activation API Endpoints """
from .swaggerFile.activation import activate_account_doc
from flask import request, jsonify, url_for
from flasgger import swag_from
from flask_jwt_extended import decode_token
from .. import limiter
from . import activation
from .. import db
from ..models.user import User
from ..models.provider import Provider



@activation.route('/activate/<token>', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(activate_account_doc)
def activate_account(token):
    """Get the token from the URL and activate the user account"""
    # Get the token from the URL
    decoded_token = decode_token(token)  # Decode the JWT token
    current_user =  decoded_token.get('sub')  # 'sub' is typically the identity
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
                {"status": "error",},
                {"message": "User dose not exist"}
                ), 407
    # Check if the account already activated
    if user.is_active == True:
        return jsonify(
        {"status": "error",},
        {"message": "Account already activated"}
        ), 200
    # If the user exists, activate the account
    user.is_active = True
    # Save the changes to the database
    db.session.commit()
    # Return a success message with a 200 status code
    return jsonify(
        {"status": "success",},
        {"message": "Account activated successfully"}
        ), 200
