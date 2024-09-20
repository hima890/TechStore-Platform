#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase
from datetime import datetime

# Adjust the path to include the 'v1' directory where the app is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import User

class UserModelTestCase(TestCase):
    def create_app(self):
        """ Set up the Flask application for testing. """
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        return app

    def setUp(self):
        """ Set up the test environment and initialize the database """
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

            # Create a sample user for testing
            user = User(
                first_name='John',
                last_name='Doe',
                username='johndoe',
                email='johndoe@test.com',
                phone_number='1234567890',
                password_hash='hashedpassword',
                is_active=True,
                gander='Male',
                location='Test Location',
                opt_code=1234,
                opt_code_time=datetime.utcnow(),
                profile_image=None
            )
            db.session.add(user)
            db.session.commit()

            self.user_id = user.id
            self.user_email = user.email

    def tearDown(self):
        """ Clean up after each test """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_user_creation(self):
        """ Test creating a new user and ensure the fields are set correctly """
        with self.app.app_context():
            user = User.query.filter_by(email='johndoe@test.com').first()
            self.assertIsNotNone(user)
            self.assertEqual(user.first_name, 'John')
            self.assertEqual(user.last_name, 'Doe')
            self.assertEqual(user.username, 'johndoe')
            self.assertEqual(user.email, 'johndoe@test.com')
            self.assertTrue(user.is_active)

    def test_user_to_dict(self):
        """ Test converting the User object to a dictionary """
        with self.app.app_context():
            user = User.query.get(self.user_id)
            user_dict = user.to_dict()
            self.assertEqual(user_dict['first_name'], 'John')
            self.assertEqual(user_dict['last_name'], 'Doe')
            self.assertEqual(user_dict['username'], 'johndoe')
            self.assertEqual(user_dict['email'], 'johndoe@test.com')
            self.assertEqual(user_dict['is_active'], True)

    def test_user_repr(self):
        """ Test the __repr__ method of the User model """
        with self.app.app_context():
            user = User.query.get(self.user_id)
            self.assertEqual(repr(user), "User email: johndoe@test.com, User name John")

if __name__ == '__main__':
    unittest.main()
