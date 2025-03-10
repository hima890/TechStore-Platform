#!/usr/bin/python3
""" Store Table Schema """
from flask import url_for
from .. import db
from datetime import datetime

class Store(db.Model):
    __tablename__ = 'stores'

    store_id = db.Column(db.Integer, primary_key=True)
    provider_id = db.Column(db.Integer, db.ForeignKey('providers.id'), nullable=False)
    store_name = db.Column(db.String(255), nullable=False)
    store_location = db.Column(db.String(255), nullable=False)
    store_email = db.Column(db.String(255), nullable=False)
    store_phone_number = db.Column(db.String(20), nullable=False)
    operation_times = db.Column(db.String(100), nullable=True)
    social_media_accounts = db.Column(db.Text, nullable=True)
    store_bio = db.Column(db.Text, nullable=True)
    inner_image = db.Column(db.String(200), nullable=True)
    outer_image = db.Column(db.String(200), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    provider = db.relationship('Provider', backref='stores', lazy=True)
    products = db.relationship('Product', backref='stores', lazy=True)
    orders = db.relationship('Order', back_populates='store')

    @property
    def inner_image_url(self):
        """ Dynamically generate the inner image URL """
        if self.inner_image:
            return 'https://techstoreplatform.tech/store_pics/' + str(self.inner_image)
        return 'https://techstoreplatform.tech/store_pics/default_inner_image.png'

    @property
    def outer_image_url(self):
        """ Dynamically generate the outer image URL """
        if self.outer_image:
            return 'https://techstoreplatform.tech/store_pics/' + str(self.outer_image)
        return 'https://techstoreplatform.tech/store_pics/default_outer_image.png'

    def __repr__(self):
        """ Return a string representation of the Store object. """
        return f"Store ID: {self.store_id}, Store Name: {self.store_name}, Provider ID: {self.provider_id}"

    def to_dict(self):
        """Convert the Store object to a dictionary."""
        return {
            'store_id': self.store_id,
            'provider_id': self.provider_id,
            'store_owner': self.provider.username,
            'store_name': self.store_name,
            'store_location': self.store_location,
            'store_email': self.store_email,
            'store_phone_number': self.store_phone_number,
            'operation_times': self.operation_times,
            'social_media_accounts': self.social_media_accounts,
            'store_bio': self.store_bio,
            'inner_image_url': self.inner_image_url,
            'outer_image_url': self.outer_image_url,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }
