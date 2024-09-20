#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase
from unittest.mock import patch
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash

# Adjust the path to include the directory where the app is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import User, Provider

class AccountManagementTestCase(TestCase):
    def create_app(self):
        """ Set up the Flask application for testing. """
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        app.config['JWT_SECRET_KEY'] = 'testsecretkey'  # Set up a secret key for JWT
        return app

    def setUp(self):
        """ Set up test app, test client, and initialize the database """
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Create a sample user for testing
            user = User(
                first_name='Test',
                last_name='User',
                username='testuser',
                email='user@test.com',
                phone_number='1234567890',
                gander='male',
                location='Test Location',
                password_hash=generate_password_hash('password123'),
                profile_image='default.jpg'
            )
            db.session.add(user)
            db.session.commit()

            self.user_id = user.id
            self.token = create_access_token(identity=user.email)

    def tearDown(self):
        """ Clean up after each test """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_get_account(self):
        """ Test retrieving the account details """
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.get('/api/v1/account', headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test', response.json['data']['first name'])

    def test_update_account(self):
        """ Test updating the account details """
        data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'username': 'updateduser',
            'phone_number': '9876543210',
            'gander': 'female',
            'location': 'New Location'
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.put('/api/v1/account-update', data=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('User account updated successfully', response.json['message'])
        self.assertEqual(response.json['data']['first name'], 'Updated')

    @patch('app.utils.saveProfilePicture', return_value=('updated_image.jpg', '/path/to/image'))
    def test_update_account_with_image(self, mock_save_profile_picture):
        """ Test updating the account details including the profile image """
        data = {
            'first_name': 'Updated',
            'last_name': 'User',
            'username': 'updateduser',
            'phone_number': '9876543210',
            'gander': 'female',
            'location': 'New Location'
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        # Simulate uploading a profile image
        image_data = {
            'profile_image': (open('tests/files/sample_image.jpg', 'rb'), 'sample_image.jpg')
        }

        response = self.client.put('/api/v1/account-update', data={**data, **image_data}, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('User account updated successfully', response.json['message'])
        self.assertEqual(response.json['data']['profile image'], 'updated_image.jpg')

    def test_update_password(self):
        """ Test updating the password """
        data = {
            'oldPassword': 'password123',
            'newPassword': 'newpassword123'
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.put('/api/v1/account-update-password', json=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('User password updated successfully', response.json['message'])

    def test_update_password_incorrect_old(self):
        """ Test updating the password with incorrect old password """
        data = {
            'oldPassword': 'wrongpassword',
            'newPassword': 'newpassword123'
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.put('/api/v1/account-update-password', json=data, headers=headers)
        self.assertEqual(response.status_code, 400)
        self.assertIn('Old password is incorrect', response.json['message'])


if __name__ == '__main__':
    unittest.main()
