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
    activation_token = db.Column(db.String(128), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        """ Create hashed password. """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """ Check hashed password. """
        return check_password_hash(self.password_hash, password)

    def generate_activation_token(self):
        """Generate a unique activation token."""
        tokenURL = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        # Return a signed string serialized with the internal serializer
        return tokenURL.dumps(self.email, salt=current_app.config['SECURITY_PASSWORD_SALT'])

    def confirm_activation_token(self, token, expiration=3600):
        """Check if the activation token is valid and not expired."""
        tokenURL = URLSafeTimedSerializer(current_app.config['SECRET_KEY'])
        # Try to deserialize the token and check if it is valid
        try:
            userEmail = tokenURL.loads(
                token,# The token to be checked
                salt=current_app.config['SECURITY_PASSWORD_SALT'],# The salt used to sign the token
                max_age=expiration # The maximum age of the token
            )
        except:
            # Return false if the token is invalid or expired
            return False
        # Return the user email from the token
        return userEmail == self.email
