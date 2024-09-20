#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase
from datetime import datetime

# Adjust the path to include the 'v1' directory where the app is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import Provider

class ProviderModelTestCase(TestCase):
    def create_app(self):
        """ Set up the Flask application for testing. """
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        return app

    def setUp(self):
        """ Set up test app, test client, and initialize the database """
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

            # Create a sample provider for testing
            provider = Provider(
                first_name='John',
                last_name='Doe',
                username='johndoe',
                email='johndoe@test.com',
                phone_number='1234567890',
                password_hash='hashedpassword',
                is_active=True,
                gander='Male',
                opt_code=1234,
                opt_code_time=datetime.utcnow(),
                profile_image=None
            )
            db.session.add(provider)
            db.session.commit()

            self.provider_id = provider.id
            self.provider_email = provider.email

    def tearDown(self):
        """ Clean up after each test """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_provider_creation(self):
        """ Test creating a new provider and ensure the fields are set correctly """
        with self.app.app_context():
            provider = Provider.query.filter_by(email='johndoe@test.com').first()
            self.assertIsNotNone(provider)
            self.assertEqual(provider.first_name, 'John')
            self.assertEqual(provider.last_name, 'Doe')
            self.assertEqual(provider.username, 'johndoe')
            self.assertEqual(provider.email, 'johndoe@test.com')
            self.assertTrue(provider.is_active)

    def test_provider_to_dict(self):
        """ Test converting the Provider object to a dictionary """
        with self.app.app_context():
            provider = Provider.query.get(self.provider_id)
            provider_dict = provider.to_dict()
            self.assertEqual(provider_dict['first_name'], 'John')
            self.assertEqual(provider_dict['last_name'], 'Doe')
            self.assertEqual(provider_dict['username'], 'johndoe')
            self.assertEqual(provider_dict['email'], 'johndoe@test.com')
            self.assertEqual(provider_dict['is_active'], True)

    def test_provider_repr(self):
        """ Test the __repr__ method of the Provider model """
        with self.app.app_context():
            provider = Provider.query.get(self.provider_id)
            self.assertEqual(repr(provider), "Provider email: johndoe@test.com, Provider name John")

if __name__ == '__main__':
    unittest.main()
