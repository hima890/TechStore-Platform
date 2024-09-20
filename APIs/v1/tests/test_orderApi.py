#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase
from flask_jwt_extended import create_access_token
from unittest.mock import patch

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import Order, Store, User

class OrdersAPITestCase(TestCase):
    def create_app(self):
        """Set up the Flask application for testing."""
        app = create_app()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'  # Use in-memory database for testing
        app.config['JWT_SECRET_KEY'] = 'testsecretkey'  # Set up a secret key for JWT
        return app

    def setUp(self):
        """Set up test app, test client, and initialize the database"""
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

            # Create a sample user and store for testing
            user = User(
                first_name='Test',
                last_name='User',
                username='testuser',
                email='testuser@example.com',
                password_hash='hashedpassword',
                phone_number='1234567890'
            )
            db.session.add(user)
            db.session.commit()

            self.user_id = user.id
            self.token = create_access_token(identity=user.email)

            store = Store(
                provider_id=self.user_id,
                store_name='Test Store',
                store_location='Test Location',
                store_email='teststore@example.com',
                store_phone_number='1234567890'
            )
            db.session.add(store)
            db.session.commit()

            self.store_id = store.store_id

    def tearDown(self):
        """Clean up after each test"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    @patch('app.utils.saveOrdersPicture', return_value=("order_img.jpg", "/path"))
    def test_add_order(self, mock_save_orders_picture):
        """Test adding an order"""
        data = {
            'name': 'John Doe',
            'email': 'johndoe@example.com',
            'store_id': self.store_id,
            'title': 'Laptop',
            'brand': 'Test Brand',
            'description': 'Test description of the laptop',
            'price': 1200.00,
            'quantity': 2,
            'img': 'order_img.jpg'
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.post('/api/v1/orders/add-order', data=data, headers=headers)
        self.assertEqual(response.status_code, 201, "Order creation failed: Expected status code 201, got {}".format(response.status_code))
        self.assertIn('Order created successfully', response.json['message'])

    def test_get_order(self):
        """Test retrieving store orders"""
        with self.app.app_context():
            # Add an order to the store
            order = Order(
                name="John Doe",
                email="johndoe@example.com",
                store_id=self.store_id,
                title="Laptop",
                brand="Test Brand",
                description="Test description of the laptop",
                price=1200.00,
                quantity=2,
                total=2400.00,
                img="order_img.jpg"
            )
            db.session.add(order)
            db.session.commit()

        data = {
            'store_id': self.store_id
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.post('/api/v1/orders/get-order', data=data, headers=headers)
        self.assertEqual(response.status_code, 200, "Get order failed: Expected status code 200, got {}".format(response.status_code))
        self.assertIn('Orders found', response.json['message'])
        self.assertGreater(len(response.json['data']), 0)  # Ensure that an order is returned

    def test_delete_order(self):
        """Test deleting an order"""
        with self.app.app_context():
            # Add an order to the store
            order = Order(
                name="John Doe",
                email="johndoe@example.com",
                store_id=self.store_id,
                title="Laptop",
                brand="Test Brand",
                description="Test description of the laptop",
                price=1200.00,
                quantity=2,
                total=2400.00,
                img="order_img.jpg"
            )
            db.session.add(order)
            db.session.commit()

            # Ensure the order is attached to the session by querying again
            order = Order.query.filter_by(email="johndoe@example.com").first()

        data = {
            'order_id': order.id
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.delete('/api/v1/orders/delete-order', data=data, headers=headers)
        self.assertEqual(response.status_code, 200, "Order deletion failed: Expected status code 200, got {}".format(response.status_code))
        self.assertIn('Order deleted successfully', response.json['message'])

if __name__ == '__main__':
    unittest.main()
