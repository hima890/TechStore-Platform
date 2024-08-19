"""
This file contains the models for the database.
"""

from blueprints import db
import datetime


class Email(db.Model):
    """
    This class is used to store the emails.
    """
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return (f"Email('{self.email}', '{self.date}')")
