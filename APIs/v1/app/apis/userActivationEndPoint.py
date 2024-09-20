#!/usr/bin/python3
""" Activation API Endpoints """
from flask import request, jsonify, url_for
from flasgger import swag_from
from flask_jwt_extended import decode_token
from .swaggerFile import activiationDoc
from . import activation
from .. import limiter
from .. import db
from ..models import User, Provider


@activation.route('/activate/<token>', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(activiationDoc)
def activate_account(token):
    """Get the token from the URL and activate the user account"""
    decoded_token = decode_token(token)
    current_user =  decoded_token.get('sub')

    if not current_user:

        return jsonify(
            {"error": "Invalid or expired token"}
            ), 400
    user = User.query.filter_by(email=current_user).first()

    if not user:
        user = Provider.query.filter_by(email=current_user).first()
        if not user:

            return jsonify(
                {"status": "error",},
                {"message": "User dose not exist"}
                ), 407

    if user.is_active == True:
        return jsonify(
        {"status": "error",},
        {"message": "Account already activated"}
        ), 200

    user.is_active = True

    db.session.commit()

    return jsonify(
        {"status": "success",},
        {"message": "Account activated successfully"}
        ), 200
