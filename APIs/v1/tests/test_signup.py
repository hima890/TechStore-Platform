# #!/usr/bin/python3
# """ Unit tests for the signup API endpoint """
# import unittest
# from unittest.mock import patch
# from io import BytesIO
# import json
# from app import create_app, db
# from app.models.user import User
# from werkzeug.security import generate_password_hash


# class SignupEndpointTests(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         """Set up the test client and database"""
#         cls.app = create_app()
#         cls.client = cls.app.test_client()
#         cls.app_context = cls.app.app_context()
#         cls.app_context.push()
#         db.create_all()

#     @classmethod
#     def tearDownClass(cls):
#         """Tear down the test database"""
#         db.session.remove()
#         db.drop_all()
#         cls.app_context.pop()

#     def test_signup_success(self):
#         """Test signup with valid data"""
#         with patch('app.utils.sendEmail.send_email') as mock_send_email, \
#              patch('app.utils.saveProfilePicture.saveProfilePicture') as mock_save_picture :

#             # Mock the profile picture saving
#             mock_save_picture.return_value = ('coming.png', './static/profile_pics')

#             response = self.client.post('/api/v1/signup', data={
#                 'name': 'testuser',
#                 'email': 'testuser@example.com',
#                 'password': 'password123',
#                 'profilePicture': './static/profile_pics/coming.png'
#             }, content_type='multipart/form-data')
#             print(str(response.status))
#             self.assertEqual(response.status_code, 201)
#             data = json.loads(response.data)
#             self.assertIn('message', data)
#             self.assertEqual(data['message'], "User created! An email was sent to activate the account.")
#             mock_send_email.assert_called_once()

#     def test_signup_missing_fields(self):
#         """Test signup with missing fields"""
#         response = self.client.post('/api/v1/signup', json={
#             'username': 'testuser',
#             'email': 'testuser@example.com'
#         })

#         self.assertEqual(response.status_code, 400)
#         data = json.loads(response.data)
#         self.assertIn('error', data)
#         self.assertEqual(data['error'], "Missing fields")

#     def test_signup_user_exists(self):
#         """Test signup with an existing user"""
#         existing_user = User(
#             name='existinguser',
#             email='existinguser@example.com',
#             password_hash=generate_password_hash('password123'),
#             is_active=True
#         )
#         db.session.add(existing_user)
#         db.session.commit()

#         response = self.client.post('/api/v1/signup', json={
#             'username': 'existinguser',
#             'email': 'existinguser@example.com',
#             'password': 'password123'
#         })

#         self.assertEqual(response.status_code, 400)
#         data = json.loads(response.data)
#         self.assertIn('error', data)
#         self.assertEqual(data['error'], 'User already exists')

#     def test_signup_server_error(self):
#         """Test signup when an error occurs during user creation"""
#         with patch('app.utils.sendEmail.send_email') as mock_send_email, \
#              patch('app.utils.saveProfilePicture.saveProfilePicture') as mock_save_picture, \
#              patch('app.models.user.User.query.filter_by') as mock_filter_by:

#             # Simulate a database error when checking for an existing user
#             mock_filter_by.side_effect = Exception('Database error')

#             response = self.client.post('/api/v1/signup', data={
#                 'name': 'testuser',
#                 'email': 'testuser@example.com',
#                 'password': 'password123',
#                 'profilePicture': './static/profile_pics/coming.png'
#             }, content_type='multipart/form-data')

#             # Ensure a server error is correctly handled and returned
#             self.assertEqual(response.status_code, 500)
#             data = json.loads(response.data)
#             self.assertIn('error', data)
#             self.assertEqual(data['error'], 'An error occurred while creating the user.')


# if __name__ == '__main__':
#     unittest.main()
