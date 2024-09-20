#!/usr/bin/python3
import os
import sys
import json
import unittest
from unittest.mock import patch
from flask_testing import TestCase

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import User, Provider


class SignupApiTestCase(TestCase):
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
            user = User(
                first_name='Test',
                last_name='User',
                username='testuser',
                email='testuser@example.com',
                phone_number='1234567890',
                password_hash='hashedpassword',
                is_active=True
            )
            db.session.add(user)
            db.session.commit()

    def tearDown(self):
        """ Clean up after each test """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    @patch('app.utils.sendEmail.send_email', return_value=True)  # Mock send_email function
    def test_signup_user(self, mock_send_email):
        """ Test user signup """
        # Mock the email sending to avoid actually sending an email
        mock_send_email.return_value = True

        data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'username': 'johndoe',
            'email': 'johndoe@example.com',
            'type': 'user',
            'phone_number': '1234567891',  # Ensure unique phone number
            'gender': 'Male',
            'location': 'Somewhere',
            'password': 'password123'
        }

        # Send a POST request with the form data
        response = self.client.post(
            '/api/v1/signup',
            data=data,  # Sending form data
            headers={'Content-Type': 'multipart/form-data'}  # Set as form-data
        )

        print(f"Response Data: {response.data}")  # Log the response data for debugging
        print(f"Response Status Code: {response.status_code}")  # Log status code

        # Ensure the response is 201 Created
        self.assertEqual(response.status_code, 201)

    @patch('app.utils.sendEmail.send_email', return_value=True)  # Mock send_email function
    def test_signup_existing_user(self, mock_send_email):
        """ Test signup when the user already exists """
        # Mock the email sending to avoid actually sending an email
        mock_send_email.return_value = True

        # Existing user data
        data = {
            'first_name': 'Test',
            'last_name': 'User',
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password123',
            'phone_number': '1234567890',
            'gender': 'Male',
            'type': 'user',
            'location': 'Somewhere'
        }

        # Try to sign up with the same email again
        response = self.client.post(
            '/api/v1/signup',
            data=data,  # Sending form data
            headers={'Content-Type': 'multipart/form-data'}  # Set as form-data
        )

        print(f"Response Data: {response.data}")  # Log the response data for debugging
        print(f"Response Status Code: {response.status_code}")  # Log status code

        # Check if the signup fails with a 409 Conflict error
        self.assertEqual(response.status_code, 409)
        json_data = json.loads(response.data)
        self.assertEqual(json_data['error'], 'User already exists')


if __name__ == '__main__':
    unittest.main()
