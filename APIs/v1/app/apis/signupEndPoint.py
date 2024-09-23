#!/usr/bin/python3
""" Signup API signUp """
from flask import request, jsonify, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from datetime import timedelta
from .swaggerFile import signuDoc, resendDoc
from . import signUp
from .. import limiter
from ..utils import send_email, saveProfilePicture
from .. import db
from ..models import User, Provider



@signUp.route('/signup', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(signuDoc)
def signup():
    """Create a new user"""

    firstName = request.form.get('first_name')
    lastName = request.form.get('last_name')
    username = request.form.get('username')
    email = request.form.get('email')
    accountType = request.form.get('type')
    phoneNumber = request.form.get('phone_number')
    ganderType = request.form.get('gender')
    userLocation = request.form.get('location')
    password = request.form.get('password')
    profilePicture = request.files.get('profile_image')

    if not username or not email or not password:
        print(str(username) + str(email) + str(password))
        return jsonify({'error': 'Missing fields'}), 400

    if User.query.filter_by(email=email).first() or Provider.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    if profilePicture:
        filename, picture_path = saveProfilePicture(profilePicture)
    else:
        filename = None

    if accountType == 'user':
        newUser = User(
            first_name=firstName,
            last_name=lastName,
            username=username,
            email=email,
            phone_number=phoneNumber,
            gander=ganderType,
            location=userLocation,
            password_hash=generate_password_hash(password),
            is_active=False,
            profile_image=filename
            )
    elif accountType == 'provider':
        newUser = Provider(
            first_name=firstName,
            last_name=lastName,
            username=username,
            email=email,
            phone_number=phoneNumber,
            gander=ganderType,
            password_hash=generate_password_hash(password),
            is_active=False,
            profile_image=filename
            )

    try:
        activationToken = create_access_token(identity=email, expires_delta=timedelta(hours=1))
        activationURL = "http://localhost:5001/api/v1/activate/{}".format(activationToken)
        plainTextContent = "Please click the link to activate your account: {}".format(activationURL)
        htmlContent = "<html><body><p>Please click the link to activate your account: <a href='{}'>Activate</a></p></body></html>".format(activationURL)

        emailFunction = send_email(
            email,
            htmlContent,
            plainTextContent,  # Add plain text content here
            "Account Activation"
        )

        if not emailFunction:
            return jsonify(
                {"status": "error",},
                {"message": "Email was not sent."},
                {'data': newUser.to_dict()}
            ), 400

        db.session.add(newUser)
        db.session.commit()

        return jsonify(
            {"status": "success",},
            {"message": "User created! Un email was sent to activate the account."},
            {'data': newUser.to_dict()}
            ), 201
    except Exception as e:
        print(e)
        db.session.rollback()
        db.session.commit()
        return jsonify({"error": "An error occurred while creating the user."}), 500


@signUp.route('/resend-confirmation', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(resendDoc)
def resendConfirmation():
    email = request.json.get('email')

    user = User.query.filter_by(email=email).first()
    if not user:
        user = Provider.query.filter_by(email=email).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
                }), 404

    if user.is_active == True:
        return jsonify({
                "status": "error",
                "message": "User acount already activated"
                }), 401

    try:
        activationToken = create_access_token(identity=email, expires_delta=timedelta(hours=1))

        activationURL = "http://localhost:5001/api/v1/activate/{}".format(activationToken)
        send_email(
            email,
            "Please click the link to activate your account: {}".format(activationURL),
            "Account Activation"
            )

        return jsonify(
            {"status": "success",},
            {"message": "Confirmation email resent. Please check your inbox."},
            ), 200
    except Exception as e:
        print(e)
        return jsonify({
            "status": "error",
            "message": "An error occurred while resending confirmation email."
            }), 500
