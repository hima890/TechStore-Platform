#!/usr/bin/python3
""" Orders Table Schema """
from flask import url_for
from .. import db
from datetime import datetime

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Foreign key to the User who placed the order
    requester_name = db.Column(db.String(100), nullable=False)  # Name of the user who requested the order
    requester_email = db.Column(db.String(120), nullable=False)  # Email of the user who requested the order
    img = db.Column(db.String(120), nullable=True)  # Product image
    title = db.Column(db.String(100), nullable=False)  # Product title
    brand = db.Column(db.String(100), nullable=False)  # Product brand
    description = db.Column(db.Text, nullable=False)  # Product description
    price = db.Column(db.Float, nullable=False)  # Product price
    quantity = db.Column(db.Integer, nullable=False)  # Quantity ordered
    total = db.Column(db.Float, nullable=False)  # Total price of the order

    # New fields for visibility
    is_visible_to_user = db.Column(db.Boolean, default=True)  # If visible to the user
    is_visible_to_provider = db.Column(db.Boolean, default=True)  # If visible to the store/provider

    user = db.relationship('User', backref='order')  # Relationship to the User model
    store = db.relationship('Store', backref='order')  # Relationship to the Store model

    def __repr__(self):
        """ Return a string representation of the Order object. """
        return "Order requester: {}, Order brand {}, Order store id {}".format(
            self.requester_name,
            self.brand,
            self.store_id
        )

    def to_dict(self):
        """Convert the Order object to a dictionary."""
        return {
            'id': self.id,
            'store_id': self.store_id,
            'user_id': self.user_id,
            'requester_name': self.requester_name,
            'requester_email': self.requester_email,
            'img': url_for('static', filename='orders_pics/' + self.img) if self.img else None,
            'title': self.title,
            'brand': self.brand,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'total': self.total,
            'is_visible_to_user': self.is_visible_to_user,
            'is_visible_to_provider': self.is_visible_to_provider
        }
