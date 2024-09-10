#!/usr/bin/python3
""" OPT API send and resend Endpoints """
from flasgger import swag_from
from .. import db
from .. import limiter
from flask import request, jsonify
from ..models.user import User
from ..models.provider import Provider
from . import optCode
from ..utils.generateOtpCode import generate_otp
from ..utils.sendEmail import send_email
from .swaggerFile.opt_Code import opt_Code




@optCode.route('/opt', methods=['POST'])
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
                "message": "User acount need to be activated"
                }), 401

    # generate OTP and creation time
    optCode, creationTime = generate_otp()
    # Save to the user table and update exicting fields
    user.opt_code = optCode
    user.opt_code_time = creationTime
    # Commit the changes to the database
    db.session.commit()

    # Send email whit the opt code to the user
    userFirstName = user.first_name
    send_email(
        email,
        """
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
        """.format(userFirstName, optCode),
        "Password reset"
    )

    # Return seccuses respound
    return jsonify({
            "status": "success",
            "message": "OPT code has been sent successful",
            "data": {
                "email": user.email
            }
        }), 200
