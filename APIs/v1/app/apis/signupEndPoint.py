#!/usr/bin/python3
""" Signup API signUp """
from flask import request, jsonify, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from .swaggerFile.swagger_docs import signup_doc
from .swaggerFile.resendSwagger import resend
from datetime import timedelta
from .. import limiter
from . import signUp
from ..utils.sendEmail import send_email
from ..utils.saveProfilePicture import saveProfilePicture
from .. import db
from ..models.user import User
from ..models.provider import Provider


@signUp.route('/signup', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(signup_doc)
def signup():
    """Create a new user"""
    # Get the data
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

    # Validate required fields
    if not username or not email or not password:
        print(str(username) + str(email) + str(password))
        return jsonify({'error': 'Missing fields'}), 400

    # Check if user already exists
    # Filter the User table by email and check if the user exists
    if User.query.filter_by(email=email).first() or Provider.query.filter_by(email=email).first():
        # Return an error message if the user already exists with a 400 status code
        return jsonify({"error": "User already exists"}), 409

    # Validate and process the profile picture
    if profilePicture:
        filename, picture_path = saveProfilePicture(profilePicture)
    else:
        filename = None  # Handle cases where no picture is uploaded

    if accountType == 'user':
        # Create a new user with is_active=False
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
        # Create a new provider with is_active=False
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
        # Save the user in the database
        db.session.add(newUser)
        db.session.commit()

        # Create an access token with a short expiration time
        activationToken = create_access_token(identity=email, expires_delta=timedelta(hours=1))

        # Send email with activation link
        activationURL = "http://localhost:5001/api/v1/activate/{}".format(activationToken)
        send_email(
            email,
            "Please click the link to activate your account: {}".format(activationURL),
            "Account Activation"
            )

        # Return a success message with the user data
        return jsonify(
            {"status": "success",},
            {"message": "User created! Un email was sent to activate the account."},
            {'data': newUser.to_dict()}
            ), 201
    except Exception as e:
        # Return to the last change
        print(e)
        db.session.rollback()
        db.session.commit()
        return jsonify({"error": "An error occurred while creating the user."}), 500


@signUp.route('/resend-confirmation', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(resend)
def resendConfirmation():
    # Get user email from the request
    email = request.json.get('email')

    # Find the user by email
    user = User.query.filter_by(email=email).first()
    if not user:
        user = Provider.query.filter_by(email=email).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
                }), 404

    # Check if the account is active
    if user.is_active == True:
        return jsonify({
                "status": "error",
                "message": "User acount already activated"
                }), 401

    try:
        # Create a new access token with a short expiration time
        activationToken = create_access_token(identity=email, expires_delta=timedelta(hours=1))

        # Send email with activation link
        activationURL = "http://localhost:5001/api/v1/activate/{}".format(activationToken)
        send_email(
            email,
            "Please click the link to activate your account: {}".format(activationURL),
            "Account Activation"
            )

        # Return a success message with the user data
        return jsonify(
            {"status": "success",},
            {"message": "Confirmation email resent. Please check your inbox."},
            ), 200
    except Exception as e:
        # Return to the last change
        print(e)
        return jsonify({
            "status": "error",
            "message": "An error occurred while resending confirmation email."
            }), 500
