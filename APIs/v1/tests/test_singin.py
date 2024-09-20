#!/usr/bin/python3
import os
import sys
import unittest
from unittest.mock import patch
from flask_testing import TestCase
from werkzeug.security import generate_password_hash

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import User, Provider


class SigninApiTestCase(TestCase):
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

            # Create a sample user for testing
            hashed_password = generate_password_hash('password123')
            user = User(
                first_name='John',
                last_name='Doe',
                username='johndoe',
                email='johndoe@example.com',
                phone_number='1234567890',
                password_hash=hashed_password,
                is_active=True
            )
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        """ Clean up after each test """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    @patch('app.utils.sendEmail.send_email', return_value=True)
    @patch('flask_jwt_extended.create_access_token', return_value="fake-token")
    def test_signin_user(self, mock_create_access_token, mock_send_email):
        """ Test user signin """
        # Ensure that the password hash checking is mocked to always pass
        with patch('werkzeug.security.check_password_hash', return_value=True):
            data = {
                'email': 'johndoe@example.com',
                'password': 'password123'
            }

            # Send a POST request to the sign-in route
            response = self.client.post(
                '/api/v1/signin',
                json=data,
                headers={'Content-Type': 'application/json'}
            )

            # Log the response data for debugging
            print(f"Response Data: {response.data.decode()}")
            print(f"Response Status Code: {response.status_code}")

            # Assert that the response status is 200
            self.assertEqual(response.status_code, 200)
            json_data = response.get_json()

            # Check if the response contains a success message and token
            self.assertEqual(json_data['status'], 'success')
            self.assertIn('token', json_data['data'])

    def test_signin_invalid_user(self):
        """ Test sign in with an invalid user """
        data = {
            'email': 'invalid@example.com',
            'password': 'password123'
        }

        # Send a POST request to the sign-in route with invalid user data
        response = self.client.post(
            '/api/v1/signin',
            json=data,
            headers={'Content-Type': 'application/json'}
        )

        # Assert that the response status is 404
        self.assertEqual(response.status_code, 404)
        json_data = response.get_json()

        # Check if the response contains an error message
        self.assertEqual(json_data['status'], 'error')
        self.assertEqual(json_data['message'], 'User not found')

    @patch('werkzeug.security.check_password_hash', return_value=False)
    def test_signin_invalid_password(self, mock_check_password_hash):
        """ Test sign in with an invalid password """
        data = {
            'email': 'johndoe@example.com',
            'password': 'wrongpassword'
        }

        # Send a POST request to the sign-in route with an invalid password
        response = self.client.post(
            '/api/v1/signin',
            json=data,
            headers={'Content-Type': 'application/json'}
        )

        # Assert that the response status is 401
        self.assertEqual(response.status_code, 401)
        json_data = response.get_json()

        # Check if the response contains an error message
        self.assertEqual(json_data['error'], 'Invalid password')


if __name__ == '__main__':
    unittest.main()
