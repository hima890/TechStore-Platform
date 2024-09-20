#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase
from flask_jwt_extended import create_access_token

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import Order, Store, Provider

class OrderModelTestCase(TestCase):
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

            # Create a sample provider and store for testing
            provider = Provider(
                first_name='Test',
                last_name='Provider',
                username='testprovider',
                email='provider@test.com',
                phone_number='0987654321',
                password_hash='hashedpassword',
                is_active=True
            )
            db.session.add(provider)
            db.session.commit()

            self.provider_id = provider.id
            self.token = create_access_token(identity=provider.email)

            # Create a sample store for testing
            store = Store(
                provider_id=self.provider_id,
                store_name='Test Store',
                store_location='Test Location',
                store_email='teststore@example.com',
                store_phone_number='1234567890'
            )
            db.session.add(store)
            db.session.commit()

            self.store_id = store.store_id

    def tearDown(self):
        """ Clean up after each test """
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_create_order(self):
        """ Test creating a new order """
        with self.app.app_context():
            # Create a sample order
            order = Order(
                store_id=self.store_id,
                name="John Doe",
                email="johndoe@example.com",
                img="order_img.jpg",
                title="Laptop",
                brand="Test Brand",
                description="Test description of the laptop",
                price=1200.00,
                quantity=2,
                total=2400.00
            )
            db.session.add(order)
            db.session.commit()

            # Query the order
            queried_order = Order.query.filter_by(email="johndoe@example.com").first()

            # Check if the order was created correctly
            self.assertIsNotNone(queried_order)
            self.assertEqual(queried_order.name, "John Doe")
            self.assertEqual(queried_order.total, 2400.00)

    def test_order_repr(self):
        """ Test the __repr__ method of the Order model """
        with self.app.app_context():
            order = Order(
                store_id=self.store_id,
                name="John Doe",
                email="johndoe@example.com",
                img="order_img.jpg",
                title="Laptop",
                brand="Test Brand",
                description="Test description of the laptop",
                price=1200.00,
                quantity=2,
                total=2400.00
            )
            db.session.add(order)
            db.session.commit()

            # Check the __repr__ method output
            expected_repr = "Order name: John Doe, Order brand Test Brand, Order store id {}".format(self.store_id)
            self.assertEqual(str(order), expected_repr)

    def test_order_to_dict(self):
        """ Test the to_dict method of the Order model """
        with self.app.app_context():
            order = Order(
                store_id=self.store_id,
                name="John Doe",
                email="johndoe@example.com",
                img="order_img.jpg",
                title="Laptop",
                brand="Test Brand",
                description="Test description of the laptop",
                price=1200.00,
                quantity=2,
                total=2400.00
            )
            db.session.add(order)
            db.session.commit()

            # Get the dictionary representation of the order
            order_dict = order.to_dict()

            # Assert that the dictionary contains the expected data
            self.assertEqual(order_dict['name'], 'John Doe')
            self.assertEqual(order_dict['price'], 1200.00)
            self.assertIn('orders_pics/order_img.jpg', order_dict['img'])

if __name__ == '__main__':
    unittest.main()
