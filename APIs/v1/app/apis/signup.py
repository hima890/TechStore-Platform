#!/usr/bin/python3
""" Signup API Endpoints """
from flask import request, jsonify, url_for
from flask_jwt_extended import create_access_token
from .. import limiter
from . import endPoints
from ..utils.sendEmail import send_email
from ..utils.saveProfilePicture import saveProfilePicture
from .. import db
from ..models.user import User


@endPoints.route('/signup', methods=['POST'])
@limiter.limit("5 per minute")
def signup():
    requestData = request.json # Get the JSON data from the request
    username = requestData.get('username') # Get the username from the JSON data
    email = requestData.get('email') # Get the email from the JSON data
    pictureFile = request.files.get('profilePicture')
    password = User.set_password(requestData.get('password')) # Get the password from the JSON data and hash it

    # Check if user already exists
    # Filter the User table by email and check if the user exists
    if User.query.filter_by(email=email).first():
        # Return an error message if the user already exists with a 400 status code
        return jsonify({"error": "User already exists"}), 400

    # Validate and process the profile picture
    if pictureFile:
        filename, picture_path = saveProfilePicture(pictureFile)
    else:
        filename = None  # Handle cases where no picture is uploaded

    # Create a new user with is_active=False
    newUser = User(
        userame=username,
        email=email,
        password=password,
        is_active=False,
        profile_pic=filename
        )

    # Save the user in the database
    try:
        db.session.add(newUser)
        db.session.commit()
        # Create an access token with a short expiration time
        activationToken = create_access_token(identity=email, expires_delta=timedelta(hours=1))

        # Send email with activation link
        activationLink = url_for('activate_account', token=activationToken, _external=True)
        send_email(
            email,
            "Please click the link to activate your account: {}".format(activationLink),
            "Account Activation"
            )
        return jsonify({"message": "User created! Un email was sent to activate the account."}), 201
    except Exception as e:
        # Return to the last change
        db.session.rollback()
        return jsonify({"error": "An error occurred while creating the user."}), 500
