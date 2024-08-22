#!/usr/bin/python3
""" User Table Schema """
from .. import db
from datetime import datetime
from flask import current_app
# Helper functions for password hashing and verification
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import URLSafeTimedSerializer



class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(50), unique=True, nullable=True)
    profile_image = db.Column(db.String(200), nullable=True)
    location = db.Column(db.String(150), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        """ Return a string representation of the User object. """
        return "User email: {}, User name {}".format(self.email, self.name)

    def to_dict(self):
        """Convert the User object to a dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

    def set_password(self, password):
        """ Create hashed password. """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ Check hashed password. """
        return check_password_hash(self.password_hash, password)

