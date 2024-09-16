#!/usr/bin/python3
""" Products mangment Endpoints """
from flask import request, jsonify
from flasgger import swag_from # type: ignore
from flask_jwt_extended import jwt_required, get_jwt_identity # type: ignore
from . import product
# from .swaggerFile import productDoc, productUpdateDoc
from ..models import User, Provider
from ..utils import saveProfilePicture
from .. import db
from .. import limiter


@product.route('/add-product', methods=['GET'])
@jwt_required()
@limiter.limit("5 per minute")
# @swag_from(accountDoc)
def addProduct():
    """Add products to the provider store account"""
    return jsonify({'message': 'Add product'}), 200
