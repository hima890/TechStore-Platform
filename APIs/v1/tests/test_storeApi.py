#!/usr/bin/python3
import os
import sys
import json
import unittest
from flask_testing import TestCase
from flask_jwt_extended import create_access_token

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import Store, Provider

class StoreApiTestCase(TestCase):
    def create_app(self):
        """ Set up the Flask application for testing. """
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        app.config['JWT_SECRET_KEY'] = 'test_secret_key'  # Mock JWT secret for testing
        return app

    def setUp(self):
        """ Set up test app, test client, and initialize the database """
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Create a sample provider for testing
            provider = Provider(
                first_name='Test',
                last_name='Provider',
                username='testprovider',
                email='provider@test.com',
                phone_number='1234567890',
                password_hash='hashedpassword',
                is_active=True
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

    def authenticate(self):
        """ Helper method to generate a JWT token for authenticated requests """
        with self.app.app_context():
            # Create an access token for the provider
            access_token = create_access_token(identity=self.provider_email)
            return f'Bearer {access_token}'

    def test_create_store(self):
        """ Test store creation """
        data = {
            'store_name': 'New Store',
            'store_location': 'Test Location',
            'store_email': 'newstore@test.com',
            'store_phone_number': '1234567890',
            'operation_times': '9 AM - 5 PM',
            'social_media_accounts': '{"facebook": "newstore"}',
            'store_bio': 'This is a new store for testing'
        }
        response = self.client.post(
            '/api/v1/stores/create-store',  # Updated URL to match the blueprint
            data=json.dumps(data),
            content_type='application/json',
            headers={'Authorization': self.authenticate()}
        )
        print(response.data)  # Add this line to debug response data
        self.assertEqual(response.status_code, 201)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'success')

    def test_update_store(self):
        """ Test updating a store """
        # First, create a store
        with self.app.app_context():
            store = Store(
                provider_id=self.provider_id,
                store_name='Old Store',
                store_location='Old Location',
                store_email='oldstore@test.com',
                store_phone_number='1234567890'
            )
            db.session.add(store)
            db.session.commit()

            # Re-query the store after the commit to avoid detached instance error
            store = db.session.get(Store, store.store_id)

        # Update the store
        update_data = {
            'store_name': 'Updated Store',
            'store_location': 'New Location',
            'store_email': 'updatedstore@test.com',
        }
        response = self.client.put(
            f'/api/v1/stores/update-store/{store.store_id}',  # Updated URL to match the blueprint
            data=json.dumps(update_data),
            content_type='application/json',
            headers={'Authorization': self.authenticate()}
        )
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'success')

    def test_delete_store(self):
        """ Test deleting a store """
        # First, create a store
        with self.app.app_context():
            store = Store(
                provider_id=self.provider_id,
                store_name='Store to Delete',
                store_location='Delete Location',
                store_email='deletestore@test.com',
                store_phone_number='1234567890'
            )
            db.session.add(store)
            db.session.commit()

            # Re-query the store after commit to avoid detached instance error
            store = db.session.get(Store, store.store_id)

        # Delete the store
        response = self.client.delete(
            f'/api/v1/stores/delete-store/{store.store_id}',  # Updated URL to match the blueprint
            headers={'Authorization': self.authenticate()}
        )
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'success')

    def test_get_all_stores(self):
        """ Test fetching all stores """
        # Create a few stores
        store_1 = Store(
            provider_id=self.provider_id,
            store_name='Store 1',
            store_location='Location 1',
            store_email='store1@test.com',
            store_phone_number='1234567890'
        )
        store_2 = Store(
            provider_id=self.provider_id,
            store_name='Store 2',
            store_location='Location 2',
            store_email='store2@test.com',
            store_phone_number='1234567891'
        )
        with self.app.app_context():
            db.session.add(store_1)
            db.session.add(store_2)
            db.session.commit()

        # Fetch all stores
        response = self.client.get('/api/v1/stores/stores')  # Updated URL to match the blueprint
        self.assertEqual(response.status_code, 200)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['status'], 'success')
        self.assertEqual(len(json_data['stores']), 2)

if __name__ == '__main__':
    unittest.main()
