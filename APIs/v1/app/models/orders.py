#!/usr/bin/python3
""" Order Table Schema """
from flask import url_for
from .. import db
from datetime import datetime


class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)  # Link to User table
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)  # Link to Store table
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)  # Link to Product table
    order_date = db.Column(db.DateTime, default=datetime.utcnow)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref='orders', lazy=True)
    store = db.relationship('Store', backref='orders', lazy=True)
    product = db.relationship('Product', backref='orders', lazy=True)

    def __repr__(self):
        """ Return a string representation of the Order object. """
        return "Order ID: {}, User ID: {}, Product ID: {}, Store ID: {}".format(self.id, self.user_id, self.product_id, self.store_id)

    def to_dict(self):
        """Convert the Order object to a dictionary."""
        return {
            'id': self.id,
            'user_id': self.user_id,
            'store_id': self.store_id,
            'product_id': self.product_id,
            'order_date': self.order_date.isoformat(),
            'quantity': self.quantity,
            'total_price': self.total_price
        }
