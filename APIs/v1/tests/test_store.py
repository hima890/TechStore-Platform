#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import Store, Provider


class StoreModelTestCase(TestCase):
    def create_app(self):
        """ Set up the Flask application for testing. """
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
        return app

    def setUp(self):
        """ Set up the test environment. """
        db.create_all()

        # Create a sample provider for testing
        self.provider = Provider(
            first_name='Test',
            last_name='Provider',
            username='testprovider',
            email='provider@test.com',
            phone_number='1234567890',
            password_hash='hashedpassword',
            is_active=True
        )
        db.session.add(self.provider)
        db.session.commit()

        # Create a sample store for testing
        self.store = Store(
            provider_id=self.provider.id,
            store_name='Test Store',
            store_location='Test Location',
            store_email='teststore@test.com',
            store_phone_number='1234567890',
            operation_times='9 AM - 5 PM',
            social_media_accounts='{"facebook": "testfb"}',
            store_bio='This is a test store.'
        )
        db.session.add(self.store)
        db.session.commit()

    def tearDown(self):
        """ Tear down the test environment. """
        db.session.remove()
        db.drop_all()

    def test_store_creation(self):
        """ Test that the store is created with the correct attributes. """
        store = Store.query.filter_by(store_name='Test Store').first()
        self.assertIsNotNone(store)
        self.assertEqual(store.store_name, 'Test Store')
        self.assertEqual(store.store_location, 'Test Location')
        self.assertEqual(store.store_email, 'teststore@test.com')
        self.assertEqual(store.store_phone_number, '1234567890')
        self.assertEqual(store.operation_times, '9 AM - 5 PM')
        self.assertEqual(store.social_media_accounts, '{"facebook": "testfb"}')
        self.assertEqual(store.store_bio, 'This is a test store.')
        self.assertEqual(store.provider_id, self.provider.id)

    def test_store_representation(self):
        """ Test the __repr__ method of the store. """
        store = Store.query.filter_by(store_name='Test Store').first()
        expected_repr = f"Store ID: {store.store_id}, Store Name: {store.store_name}, Provider ID: {store.provider_id}"
        self.assertEqual(repr(store), expected_repr)

    def test_store_to_dict(self):
        """ Test that the to_dict method returns the correct data. """
        store = Store.query.filter_by(store_name='Test Store').first()
        store_dict = store.to_dict()
        self.assertEqual(store_dict['store_name'], 'Test Store')
        self.assertEqual(store_dict['store_location'], 'Test Location')
        self.assertEqual(store_dict['store_email'], 'teststore@test.com')
        self.assertEqual(store_dict['store_phone_number'], '1234567890')
        self.assertEqual(store_dict['operation_times'], '9 AM - 5 PM')
        self.assertEqual(store_dict['social_media_accounts'], '{"facebook": "testfb"}')
        self.assertEqual(store_dict['store_bio'], 'This is a test store.')
        self.assertIn('inner_image_url', store_dict)
        self.assertIn('outer_image_url', store_dict)
        self.assertIn('created_at', store_dict)
        self.assertIn('updated_at', store_dict)


if __name__ == '__main__':
    unittest.main()
