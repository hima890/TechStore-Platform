#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import Product, Store, Provider


class ProductModelTestCase(TestCase):
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

            # Create a sample provider for testing, since store requires a provider_id
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

            # Create a sample store for testing, since product requires a store_id
            store = Store(
                provider_id=provider.id,
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

    def test_create_product(self):
        """ Test creating a new product """
        with self.app.app_context():
            # Create a sample product
            product = Product(
                store_id=self.store_id,
                name="Sample Product",
                product_id="P12345",
                brand="Test Brand",
                category="Electronics",
                description="A sample product description",
                price=100.0,
                deliveryStatus=True,
                image_1="image1.jpg",
                image_2="image2.jpg",
                image_3="image3.jpg",
                image_4="image4.jpg"
            )
            db.session.add(product)
            db.session.commit()

            # Query the product
            queried_product = Product.query.filter_by(product_id="P12345").first()

            # Check if the product was created correctly
            self.assertIsNotNone(queried_product)
            self.assertEqual(queried_product.name, "Sample Product")
            self.assertEqual(queried_product.price, 100.0)

    def test_product_repr(self):
        """ Test the __repr__ method of the Product model """
        with self.app.app_context():
            product = Product(
                store_id=self.store_id,
                name="Sample Product",
                product_id="P12345",
                brand="Test Brand",
                category="Electronics",
                description="A sample product description",
                price=100.0,
                deliveryStatus=True,
                image_1="image1.jpg",
                image_2="image2.jpg",
                image_3="image3.jpg",
                image_4="image4.jpg"
            )
            db.session.add(product)
            db.session.commit()

            # Check the __repr__ method output
            expected_repr = "Product name: Sample Product, Product brand Test Brand, Product store id {}".format(self.store_id)
            self.assertEqual(str(product), expected_repr)

    def test_product_to_dect(self):
        """ Test the to_dect method of the Product model """
        with self.app.app_context():
            product = Product(
                store_id=self.store_id,
                name="Sample Product",
                product_id="P12345",
                brand="Test Brand",
                category="Electronics",
                description="A sample product description",
                price=100.0,
                deliveryStatus=True,
                image_1="image1.jpg",
                image_2="image2.jpg",
                image_3="image3.jpg",
                image_4="image4.jpg"
            )
            db.session.add(product)
            db.session.commit()

            # Get the dictionary representation of the product
            product_dict = product.to_dect()

            # Assert that the dictionary contains the expected data
            self.assertEqual(product_dict['name'], 'Sample Product')
            self.assertEqual(product_dict['price'], 100.0)
            self.assertIn('image_1', product_dict)
            self.assertIn('product_images/image1.jpg', product_dict['image_1'])


if __name__ == '__main__':
    unittest.main()
