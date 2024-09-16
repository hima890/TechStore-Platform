#!/usr/bin/python3
""" Product Table Schema """
from flask import url_for
from .. import db
from datetime import datetime


class Product(db.Model):
    __tablename__ = 'product'
    id = db.Column(db.Integer, primary_key=True)
    store_id = db.Column(db.Integer, db.ForeignKey('stores.store_id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    brand = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    deliveryStatus =  db.Column(db.Boolean, default=False)
    image_1 = db.Column(db.String(255), nullable=False)
    image_2 = db.Column(db.String(255), nullable=False)
    image_3 = db.Column(db.String(255), nullable=False)
    image_4 = db.Column(db.String(255), nullable=False)


    def __repr__(self):
        """ Return a string representation of the Product object. """
        return "Product name: {}, Product brand {}, Product store id {}".format(
            self.name,
            self.brand,
            self.store_id
            )
    def to_dect(self):
        """Convert the Product object to a dictionary."""
        # Return the product data as a dictionary
        return {
            'id': self.id,
            'store_id': self.store_id,
            'name': self.name,
            'brand': self.brand,
            'category': self.category,
            'description': self.description,
            'price': self.price,
            'deliveryStatus': self.deliveryStatus,
            'image_1': self.image_1,
            'image_2': self.image_2,
            'image_3': self.image_3,
            'image_4': self.image_4
        }
