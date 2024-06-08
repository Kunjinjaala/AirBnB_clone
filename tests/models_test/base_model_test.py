#!/usr/bin/python3
"""Test script for testing the BaseModel Class"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch
import uuid


class TestBaseModel(unittest.TestCase):
    """Test the BaseModel class"""

    def setUp(self):
        """Set up the test environment"""
        self.model = BaseModel()

    def tearDown(self):
        """Clean up after each test"""
        del self.model

    def test_id_is_unique(self):
        """Test that id is a unique string"""
        other_model = BaseModel()
        self.assertNotEqual(self.model.id, other_model.id)
        self.assertIsInstance(self.model.id, str)

    def test_created_at(self):
        """Test that created_at is a datetime object"""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at(self):
        """Test that updated_at is a datetime object and is updated"""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(self.model.updated_at, old_updated_at)
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_method(self):
        """Test the __str__ method"""
        string = str(self.model)
        self.assertIn(f"[{self.model.__class__.__name__}]", string)
        self.assertIn(f"({self.model.id})", string)
        self.assertIn(f"'id': '{self.model.id}'", string)

    def test_to_dict(self):
        """Test the to_dict method"""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_kwargs(self):
        """Test creating instance with kwargs"""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)
        self.assertNotEqual(self.model, new_model)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test the save method"""
        self.model.save()
        self.assertTrue(mock_storage.save.called)

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test that new is called in init"""
        model = BaseModel()
        self.assertTrue(mock_storage.new.called)


if __name__ == "__main__":
    unittest.main()
