#!/usr/bin/python3
""" Proudcts Table Schema """
from flask import url_for
from .. import db
from datetime import datetime


class Order(db.Model):
    __tablename__ =  'orders'

    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    img = db.Column(db.String(120), nullable=True)
    title = db.Column(db.String(100), nullable=False)
    brand = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __repr__(self):
        """ Return a string representation of the Order object. """
        return "Order name: {}, Order brand {}, Order store id {}".format(
            self.name,
            self.brand,
            self.store_id
            )

    def to_dict(self):
        """Convert the Order object to a dictionary."""
        # Return the order data as a dictionary
        return {
            'id': self.id,
            'store_id': self.store_id,
            'name': self.name,
            'email': self.email,
            'img': url_for('static', filename='orders_pics/' + self.img) if self.img else None,
            'title': self.title,
            'brand': self.brand,
            'description': self.description,
            'price': self.price,
            'quantity': self.quantity,
            'total': self.total
        }
