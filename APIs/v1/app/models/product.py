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
    product_id = db.Column(db.String(10), nullable=False, unique=True)
    brand = db.Column(db.String(255), nullable=False)
    category = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Float, nullable=False)
    deliveryStatus = db.Column(db.Boolean, default=False)
    image_1 = db.Column(db.String(255), nullable=False)  # Only one image now

    def __repr__(self):
        """ Return a string representation of the Product object. """
        return "Product name: {}, Product brand {}, Product store id {}".format(
            self.name,
            self.brand,
            self.store_id
        )

    def to_dict(self):
        """Convert the Product object to a dictionary."""
        return {
            'id': self.id,
            'store_id': self.store_id,
            'name': self.name,
            'brand': self.brand,
            'category': self.category,
            'description': self.description,
            'price': self.price,
            'deliveryStatus': self.deliveryStatus,
            'product_id' : self.product_id,
            'image_1': 'https://techstoreplatform.tech/products_images/' + str(self.image_1) if self.image_1 else None
        }