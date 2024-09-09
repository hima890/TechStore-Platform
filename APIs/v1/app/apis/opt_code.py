#!/usr/bin/python3
""" OPT API Endpoints """
from flasgger import swag_from
from .. import limiter
from flask import request, jsonify
from ..models.user import User
from ..models.provider import Provider
from . import optCode


@optCode.route('/opt', methods=['GET'])
@limiter.limit("5 per minute")
def sendNewOptCode():
    return jsonify(
        {"endpoint works"}
    )