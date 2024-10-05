#!/usr/bin/python3
""" OPT API send and resend Endpoints """
from flask import request, jsonify
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from datetime import timedelta
from . import optCode
from .swaggerFile import optCodeDoc, verifyDoc
from ..models import User, Provider
from .. import db
from .. import limiter
from ..utils import generate_otp, send_email, isOtpValid


@optCode.route('/opt', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(optCodeDoc)
def sendNewOptCode():
    data = request.get_json()
    email = data.get('email')

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

    optCode, creationTime = generate_otp()
    user.opt_code = optCode
    user.opt_code_time = creationTime
   
    userFirstName = "User"
    plainTextContent = """\
    Dear {},

    We received a request to reset your password. Please use the One-Time Password (OTP) below to reset your password. This code is valid for the next 10 minutes.

    Your OTP Code: {}

    If you did not request a password reset, please ignore this email or contact our support team immediately.

    Best regards,
    TechStore Support Team

    Note: For security reasons, this code will expire after 10 minutes.
    """.format(userFirstName, optCode)

    htmlContent = """\
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Password Reset OTP</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            }}
            h1 {{
                color: #333333;
                font-size: 24px;
            }}
            p {{
                color: #555555;
                font-size: 16px;
            }}
            .otp-code {{
                font-size: 22px;
                color: #1a73e8;
                font-weight: bold;
            }}
            .footer {{
                margin-top: 20px;
                color: #999999;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Password Reset Request</h1>
            <p>Dear <strong>{}</strong>,</p>
            <p>We received a request to reset your password. Please use the One-Time Password (OTP) below to reset your password. This code is valid for the next 10 minutes.</p>
            
            <p class="otp-code">Your OTP Code: <strong>{}</strong></p>
            
            <p>If you did not request a password reset, please ignore this email or contact our support team immediately.</p>
            
            <p>Best regards,<br><strong>TechStore</strong> Support Team</p>
            
            <p class="footer">Note: For security reasons, this code will expire after 10 minutes.</p>
        </div>
    </body>
    </html>
    """.format(userFirstName, optCode)

    # Call the send_email function with both plain text and HTML content
    emailFunction = send_email(
        email,
        htmlContent,        # HTML version
        plainTextContent,   # Plain text version
        "Password reset"    # Subject
    )
    # Check of the email was sent successfully
    if not emailFunction:
        return jsonify({
            "status": "error",
            "message": "OTP code email was not sent."
        }), 400

    # Save the OPT code to the database
    db.session.commit()
    # Retrun success message
    return jsonify({
            "status": "success",
            "message": "OPT code has been sent successful",
            "data": {
                "email": user.email
            }
        }), 200



@optCode.route('/otp-verify', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(verifyDoc)
def verify():
    data = request.get_json()
    otpCode = int(data.get('otpCode'))

    user = User.query.filter_by(opt_code=otpCode).first()
    if not user:
        user = Provider.query.filter_by(opt_code=otpCode).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "Invalid OPT code"
                }), 401

    otpCreationTime = user.opt_code_time
    if not isOtpValid(otpCreationTime):
        return jsonify({
                "status": "error",
                "message": "Invalid OTP code, time out"
                }), 404
    else:

        email = user.email
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
                    "token": access_token
                }
            }), 200

        except Exception as e:
            print("{}".format(e))
            return jsonify({
                "status": "error",
                "message": "An error occurred while authenicate the user."
                }), 500
