#!/usr/bin/python3
""" Provider Table Schema """
from flask import url_for
from .. import db
from datetime import datetime


class Provider(db.Model):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(150), nullable=False)
    last_name = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(50), unique=True, nullable=True)
    profile_image = db.Column(db.String(200), nullable=True)
    gander = db.Column(db.String(50), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        """ Return a string representation of the Provider object. """
        return "Provider email: {}, Provider name {}".format(self.email, self.first_name)

    def to_dict(self):
        """Convert the Provider object to a dictionary."""
        # Check if the provider has a profile image
        if self.profile_image:
            profile_image_url = url_for('static', filename='profile_pics' + self.profile_image)
        else:
            # Set a default profile image
            profile_image_url = 'defult_profile_image.png'
        # Return the provider data as a dictionary
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'gander': self.gander,
            'is_active': self.is_active,
            'profile_image_path': profile_image_url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
