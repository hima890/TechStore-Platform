#!/usr/bin/python3
""" Account management Endpoints """
from flask import request, jsonify
from flasgger import swag_from
from flask_jwt_extended import jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from . import account
from .swaggerFile import accountDoc, accountUpdateDoc, accountUpdatePasswordDoc
from ..models import User, Provider
from ..utils import saveProfilePicture
from .. import db
from .. import limiter


@account.route('/account', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(accountDoc)
def getAccount():
    """Get the user's account"""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400
    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        user = Provider.query.filter_by(email=currentUserEmail).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404

    return jsonify({
        "status": "success",
        "data": {
            "userId": user.id,
            "first name": user.first_name,
            "last name": user.last_name,
            "username": user.username,
            "email": user.email,
            "phone number": user.phone_number,
            "gander": user.gander,
            "location": user.location,
            "profile image": user.profile_image,
        }
    }), 200


@account.route('/account-update', methods=['PUT'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(accountUpdateDoc)
def updateAccount():
    """Update the user's account"""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400
    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        user = Provider.query.filter_by(email=currentUserEmail).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404

    if not request.form:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
        }), 400

    if request.form.get("first_name"):
        user.first_name = request.form.get("first_name")
    if request.form.get("last_name"):
        user.last_name = request.form.get("last_name")
    if request.form.get("username"):
        user.username = request.form.get("username")
    if request.form.get("phone_number"):
        user.phone_number = request.form.get("phone_number")
    if request.form.get("gander"):
        user.gander = request.form.get("gander")
    if request.form.get("location"):
        user.location = request.form.get("location")
    if request.form.get("email"):
        user.email = request.form.get("email")

    file = request.files.get('profile_image')
    if file:
        filename, picture_path = saveProfilePicture(file)
        user.profile_image = filename

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User account updated successfully",
        "data": {
            "userId": user.id,
            "first name": user.first_name,
            "last name": user.last_name,
            "username": user.username,
            "email": user.email,
            "phone number": user.phone_number,
            "gander": user.gander,
            "location": user.location,
            "profile image": user.profile_image
        }
    }), 200


@account.route('/account-update-password', methods=['PUT'])
@jwt_required()
@limiter.limit("5 per minute")
@swag_from(accountUpdatePasswordDoc)
def updatePassword():
    """Update the user's password"""
    currentUserEmail = get_jwt_identity()
    if not currentUserEmail:
        return jsonify({
            "status": "error",
            "message": "Bad request, no user token"
        }), 400

    user = User.query.filter_by(email=currentUserEmail).first()
    if not user:
        user = Provider.query.filter_by(email=currentUserEmail).first()
        if not user:
            return jsonify({
                "status": "error",
                "message": "User not found"
            }), 404

    data = request.get_json()
    if not data:
        return jsonify({
            "status": "error",
            "message": "Bad request, no data provided"
        }), 400

    oldPassword = data.get("oldPassword")
    newPassword = data.get("newPassword")
 
    if not oldPassword or not newPassword:
        return jsonify({
            "status": "error",
            "message": "Bad request, oldPassword and newPassword are required"
        }), 400

    if not check_password_hash(user.password_hash, oldPassword):
        return jsonify({
            "status": "error",
            "message": "Old password is incorrect"
        }), 400

    user.password_hash = newPassword

    db.session.commit()

    return jsonify({
        "status": "success",
        "message": "User password updated successfully",
        "data": {
            "userId": user.id,
            "first name": user.first_name,
            "last name": user.last_name,
            "username": user.username,
            "email": user.email,
            "phone number": user.phone_number,
            "gander": user.gander,
            "location": user.location,
            "profile image": user.profile_image
        }
    }), 200
