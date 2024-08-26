#!/usr/bin/python3
""" Signup API Endpoints """
from flask import request, jsonify, url_for
from werkzeug.security import generate_password_hash,check_password_hash
from flask_jwt_extended import create_access_token
from flasgger import swag_from
from .swagger_docs import signup_doc
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
    if request.content_type == 'application/json':
        data = request.get_json()
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        profilePicture = data.get('profile_image')  # No file upload in JSON
    elif 'multipart/form-data' in request.content_type:
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        profilePicture = request.files.get('profile_image')
    else:
        return jsonify({'error': 'Unsupported Media Type'}), 415

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
        print(str(filename) + ' ' + str(picture_path))
    else:
        filename = None  # Handle cases where no picture is uploaded
        print("nothinf")

    # Create a new user with is_active=False
    newUser = User(
        name=username,
        email=email,
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
        activationURL = url_for('endPoints.activateAccount', token=activationToken, _external=True)
        send_email(
            email,
            "Please click the link to activate your account: {}".format(activationURL),
            "Account Activation"
            )
        return jsonify({"message": "User created! Un email was sent to activate the account."}), 201
    except Exception as e:
        # Return to the last change
        print("The server error: " + str(e))
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the user."}), 500

@endPoints.route('/activate/<token>', methods=['GET'])
def activateAccount(token):
    # Your activation logic here
    return "Account activated!"
