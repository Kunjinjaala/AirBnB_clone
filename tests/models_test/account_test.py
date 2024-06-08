#!/usr/bin/python3
"""Test script for testing the User Class"""
import unittest
from models.user import User
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestUser(unittest.TestCase):
    """Test the User class"""

    def setUp(self):
        """Set up the test environment"""
        self.user = User()

    def tearDown(self):
        """Clean up after each test"""
        del self.user

    def test_is_instance(self):
        """Test if user is an instance of BaseModel"""
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """Test the attributes of User"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        user_dict = self.user.to_dict()
        self.assertEqual(user_dict['__class__'], 'User')
        self.assertEqual(type(user_dict['created_at']), str)
        self.assertEqual(type(user_dict['updated_at']), str)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.user.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.user.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method"""
        self.user.email = "user@example.com"
        string = str(self.user)
        self.assertIn("[User]", string)
        self.assertIn("'email': 'user@example.com'", string)

    def test_save_method(self):
        """Test save method"""
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)

    def test_kwargs(self):
        """Test creating instance with kwargs"""
        user_dict = self.user.to_dict()
        new_user = User(**user_dict)
        self.assertEqual(self.user.id, new_user.id)
        self.assertEqual(self.user.created_at, new_user.created_at)
        self.assertEqual(self.user.updated_at, new_user.updated_at)
        self.assertNotEqual(self.user, new_user)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test the save method"""
        self.user.save()
        self.assertTrue(mock_storage.save.called)

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test that new is called in init"""
        user = User()
        self.assertTrue(mock_storage.new.called)


if __name__ == "__main__":
    unittest.main()
