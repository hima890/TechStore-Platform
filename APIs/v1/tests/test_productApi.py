#!/usr/bin/python3
import os
import sys
import unittest
from flask_testing import TestCase
from unittest.mock import patch
from flask_jwt_extended import create_access_token

# Adjust the path to include the 'v1' directory where app.py is located
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', 'v1')))

from app import create_app, db  # Import from the 'v1' directory
from app.models import Product, Store, Provider


class ProductManagementTestCase(TestCase):
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

    @patch('app.utils.saveProductImages', return_value=(["image1.jpg", "image2.jpg", "image3.jpg", "image4.jpg"], '/path'))
    @patch('app.utils.generateProductId', return_value='P12345')
    def test_add_product(self, mock_generate_product_id, mock_save_product_images):
        """ Test adding a product """
        data = {
            'store_id': self.store_id,
            'name': 'Test Product',
            'brand': 'Test Brand',
            'category': 'Test Category',
            'description': 'Test Description',
            'price': 99.99,
            'status': True
        }
        files = {
            'image_1': (open('tests/files/image1.jpg', 'rb'), 'image1.jpg'),
            'image_2': (open('tests/files/image2.jpg', 'rb'), 'image2.jpg'),
            'image_3': (open('tests/files/image3.jpg', 'rb'), 'image3.jpg'),
            'image_4': (open('tests/files/image4.jpg', 'rb'), 'image4.jpg')
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.post('/api/v1/products/add-product', data=data, content_type='multipart/form-data', headers=headers, files=files)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product added successfully', response.json['message'])

    @patch('app.utils.updateProductImage', return_value=('updated_image.jpg', '/path'))
    def test_update_product(self, mock_update_product_image):
        """ Test updating a product """
        with self.app.app_context():
            product = Product(
                store_id=self.store_id,
                name="Test Product",
                product_id="P12345",
                brand="Test Brand",
                category="Test Category",
                description="Test Description",
                price=99.99,
                deliveryStatus=True,
                image_1="image1.jpg",
                image_2="image2.jpg",
                image_3="image3.jpg",
                image_4="image4.jpg"
            )
            db.session.add(product)
            db.session.commit()

        data = {
            'product_id': 'P12345',
            'name': 'Updated Product',
            'brand': 'Updated Brand',
            'category': 'Updated Category',
            'price': 150.0
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.put('/api/v1/products/update-product', data=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product updated successfully', response.json['message'])

    @patch('app.utils.deleteProductImage', return_value=True)
    def test_delete_product(self, mock_delete_product_image):
        """ Test deleting a product """
        with self.app.app_context():
            product = Product(
                store_id=self.store_id,
                name="Test Product",
                product_id="P12345",
                brand="Test Brand",
                category="Test Category",
                description="Test Description",
                price=99.99,
                deliveryStatus=True,
                image_1="image1.jpg",
                image_2="image2.jpg",
                image_3="image3.jpg",
                image_4="image4.jpg"
            )
            db.session.add(product)
            db.session.commit()

        data = {
            'product_id': 'P12345'
        }
        headers = {
            'Authorization': f'Bearer {self.token}'
        }

        response = self.client.delete('/api/v1/products/delete-product', data=data, headers=headers)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Product deleted successfully', response.json['message'])

    def test_get_all_products(self):
        """ Test retrieving all products """
        with self.app.app_context():
            product1 = Product(
                store_id=self.store_id,
                name="Test Product 1",
                product_id="P12345",
                brand="Test Brand",
                category="Category 1",
                description="Test Description",
                price=99.99,
                deliveryStatus=True,
                image_1="image1.jpg",
                image_2="image2.jpg",
                image_3="image3.jpg",
                image_4="image4.jpg"
            )
            product2 = Product(
                store_id=self.store_id,
                name="Test Product 2",
                product_id="P67890",
                brand="Test Brand 2",
                category="Category 2",
                description="Test Description",
                price=199.99,
                deliveryStatus=True,
                image_1="image1.jpg",
                image_2="image2.jpg",
                image_3="image3.jpg",
                image_4="image4.jpg"
            )
            db.session.add(product1)
            db.session.add(product2)
            db.session.commit()

        response = self.client.get('/api/v1/products/get-products')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Products successfully retrieved', response.json['message'])


if __name__ == '__main__':
    unittest.main()
