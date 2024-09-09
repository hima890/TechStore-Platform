#!/usr/bin/python3
""" OPT API Endpoints """
from flasgger import swag_from
from .. import limiter
from flask import request, jsonify
from ..models.user import User
from ..models.provider import Provider
from . import optCode
from .utils import generateOtpCode


@optCode.route('/opt', methods=['GET'])
@limiter.limit("5 per minute")
def sendNewOptCode():
    # Get the user account email
    data = request.get_json()
    email = data.get('email')

    # Check if the account excit
    user = User.query.filter_by(email=email).first()
    if not user:
        user = Provider.query.filter_by(email=email).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
                }), 404

    # Check if the account is active
    if user.is_active != True:
        return jsonify({
                "status": "error",
                "message": "User acoount need to be activated"
                }), 401

    # 
