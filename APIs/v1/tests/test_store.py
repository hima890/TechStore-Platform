#!/usr/bin/python3

import os
import sys
import unittest
from flask import Flask
from flask_testing import TestCase
from flask_jwt_extended import create_access_token

# Add the v1 directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Provider, Store

class StoreTestCase(TestCase):
    def create_app(self):
        # Set up the Flask application for testing
        app = create_app()
        app.config['TESTING'] = True
        
        # Dynamically set the SQLite database path relative to the project directory
        base_dir = os.path.abspath(os.path.dirname(__file__))
        db_path = os.path.join(base_dir, 'databases', 'test_database.db')
        
        # Ensure the directory for the database exists
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

        # Use the dynamically generated database path
        app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
        app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this in production
        return app

    def setUp(self):
        # Create tables and seed the database with test data
        db.create_all()
        self.provider = Provider(
            first_name='Test',
            last_name='Provider',
            username='testprovider',
            email='test@provider.com',
            phone_number='1234567890',
            gander='male',
            password_hash='hashedpassword',
            is_active=True
        )
        db.session.add(self.provider)
        db.session.commit()

        # Generate a JWT token for the provider
        self.access_token = create_access_token(identity=self.provider.email)

        # Create a store to be used in update and delete tests
        self.store = Store(
            provider_id=self.provider.id,
            store_name='Test Store',
            store_location='Test Location',
            store_email='teststore@example.com',
            store_phone_number='1234567890',
            operation_times='9 AM - 5 PM',
            social_media_accounts='{"facebook": "testfb", "twitter": "testtw"}',
            store_bio='This is a test store.'
        )
        db.session.add(self.store)
        db.session.commit()

    def tearDown(self):
        # Drop all tables after each test
        db.session.remove()
        db.drop_all()

    def test_create_store(self):
        # Create a store with all required fields
        response = self.client.post(
            '/api/v1/stores/create-store',
            data={
                'store_name': 'New Test Store',
                'store_location': 'New Test Location',
                'store_email': 'newstore@example.com',
                'store_phone_number': '0987654321',
                'operation_times': '10 AM - 6 PM',
                'social_media_accounts': '{"facebook": "newfb", "twitter": "newtw"}',
                'store_bio': 'This is another test store.',
            },
            headers={
                'Authorization': f'Bearer {self.access_token}'  # Include JWT token in headers
            },
            content_type='multipart/form-data'
        )

        self.assertEqual(response.status_code, 201)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Store successfully created!')
        self.assertIn('data', data)
        self.assertEqual(data['data']['store_name'], 'New Test Store')
        self.assertEqual(data['data']['store_location'], 'New Test Location')
        self.assertEqual(data['data']['store_email'], 'newstore@example.com')
        self.assertEqual(data['data']['store_phone_number'], '0987654321')

    def test_update_store(self):
        # Update the existing store
        response = self.client.put(
            f'/api/v1/stores/update-store/{self.store.store_id}',
            data={
                'store_name': 'Updated Test Store',
                'store_location': 'Updated Location',
                'store_email': 'updatedstore@example.com',
                'store_phone_number': '5555555555',
                'operation_times': '11 AM - 7 PM'
            },
            headers={
                'Authorization': f'Bearer {self.access_token}'  # Include JWT token in headers
            },
            content_type='multipart/form-data'
        )

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Store updated successfully!')
        self.assertIn('data', data)
        self.assertEqual(data['data']['store_name'], 'Updated Test Store')
        self.assertEqual(data['data']['store_location'], 'Updated Location')
        self.assertEqual(data['data']['store_email'], 'updatedstore@example.com')
        self.assertEqual(data['data']['store_phone_number'], '5555555555')

    def test_delete_store(self):
        # Delete the existing store
        response = self.client.delete(
            f'/api/v1/stores/delete-store/{self.store.store_id}',
            headers={
                'Authorization': f'Bearer {self.access_token}'  # Include JWT token in headers
            }
        )

        self.assertEqual(response.status_code, 200)
        data = response.get_json()
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Store deleted successfully')  # Ensure this matches the exact API response


if __name__ == '__main__':
    unittest.main()
