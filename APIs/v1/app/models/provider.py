#!/usr/bin/python3
""" Provider Table Schema """
from flask import url_for
from .. import db
from datetime import datetime


class Provider(db.Model):
    __tablename__ = 'providers'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    phone_number = db.Column(db.String(50), unique=False, nullable=True)
    gander = db.Column(db.String(50), nullable=True)
    account_type = db.Column(db.String(150), nullable=True)    
    password_hash = db.Column(db.String(512), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    opt_code = db.Column(db.Integer, nullable=True)
    opt_code_time = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        """ Return a string representation of the Provider object. """
        return "Provider email: {}, Provider name {}".format(self.email, self.first_name)

    def to_dict(self):
        """Convert the Provider object to a dictionary."""
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone_number': self.phone_number,
            'gander': self.gander,
            'is_active': self.is_active,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'account_type': self.account_type
        }
