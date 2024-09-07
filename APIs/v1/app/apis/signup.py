#!/usr/bin/python3
""" Signup API Endpoints """
from flask import request, jsonify, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from .swaggerFile.swagger_docs import signup_doc
from datetime import timedelta
from .. import limiter
from . import endPoints
from ..utils.sendEmail import send_email
from ..utils.saveProfilePicture import saveProfilePicture
from .. import db
from ..models.user import User


@endPoints.route('/signup', methods=['POST'])
@limiter.limit("5 per minute")
@swag_from(signup_doc)
def signup():
    """Create a new user"""
    if request.content_type == 'application/json':
        data = request.get_json()
        firstName = data.get('first_name')
        lastName = data.get('last_name')
        username = data.get('username')
        email = data.get('email')
        type = data.get('type')
        phoneNumber = data.get('phone_number')
        ganderType = data.get('gender')
        userLocation = data.get('location')
        password = data.get('password')
        profilePicture = request.files.get('profile_image')  # No file upload in JSON
    elif 'multipart/form-data' in request.content_type:
        firstName = request.form.get('first_name')
        lastName = request.form.get('last_name')
        username = request.form.get('username')
        email = request.form.get('email')
        type = request.form.get('type')
        phoneNumber = request.form.get('phone_number')
        ganderType = request.form.get('gender')
        userLocation = request.form.get('location')
        password = request.form.get('password')
        profilePicture = request.files.get('profile_image')
    else:
        return jsonify({'error': 'Unsupported Request Type'}), 415

    # Validate required fields
    if not username or not email or not password:
        print(str(username) + str(email) + str(password))
        return jsonify({'error': 'Missing fields'}), 400

    # Check if user already exists
    # Filter the User table by email and check if the user exists
    if User.query.filter_by(email=email).first():
        # Return an error message if the user already exists with a 400 status code
        return jsonify({"error": "User already exists"}), 409

    # Validate and process the profile picture
    if profilePicture:
        filename, picture_path = saveProfilePicture(profilePicture)
    else:
        filename = None  # Handle cases where no picture is uploaded

    # Create a new user with is_active=False
    newUser = User(
        first_name=firstName,
        last_name=lastName,
        username=username,
        email=email,
        phone_number=phoneNumber,
        type=type,
        gander=ganderType,
        location=userLocation,
        password_hash=generate_password_hash(password),
        is_active=False,
        profile_image=filename
        )

    # Save the user in the database
    try:
        db.session.add(newUser)
        db.session.commit()
        # Create an access token with a short expiration time
        activationToken = create_access_token(identity=email, expires_delta=timedelta(hours=1))

        # Send email with activation link
        activationURL = "http://localhost:5001/api/v1/activate?token={}".format(activationToken)
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
