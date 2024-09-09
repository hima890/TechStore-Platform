#!/usr/bin/python3
""" OPT API Endpoints """
from flasgger import swag_from
from .. import db
from .. import limiter
from flask import request, jsonify
from ..models.user import User
from ..models.provider import Provider
from . import optCode
from .utils import generateOtpCode
from ..utils.sendEmail import send_email
from from .swaggerFile.swagger_docs import signup_d



@optCode.route('/opt', methods=['GET'])
@limiter.limit("5 per minute")
@swag_from(opt_Code)
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

    # generate OTP and creation time
    optCode, creationTime = generateOtpCode()
    # Save to the user table and update exicting fields
    user.opt_code = optCode
    user.opt_code_time = creationTime
    # Commit the changes to the database
    db.session.commit()

    # Send email whit the opt code to the user
    userFirstName = user.
    send_email(
            email,
            """
            Dear {},

            We received a request to reset your password. Please use the One-Time Password (OTP) below to reset your password. This code is valid for the next 10 minutes.

            Your OTP Code: {}

            If you did not request a password reset, please ignore this email or contact our support team immediately.

            Best regards,  
            TechStore Support Team

            Note: For security reasons, this code will expire after 10 minutes.

            """.format(
                first_name,
                optCode
            )
            )
