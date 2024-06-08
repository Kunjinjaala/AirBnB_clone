#!/usr/bin/python3
"""Test script for testing the State Class"""
import unittest
from models.state import State
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch

class TestState(unittest.TestCase):
    """Test the State class"""

    def setUp(self):
        """Set up the test environment"""
        self.state = State()

    def tearDown(self):
        """Clean up after each test"""
        del self.state

    def test_is_instance(self):
        """Test if state is an instance of BaseModel"""
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """Test the attributes of State"""
        self.assertEqual(self.state.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        state_dict = self.state.to_dict()
        self.assertEqual(state_dict['__class__'], 'State')
        self.assertEqual(type(state_dict['created_at']), str)
        self.assertEqual(type(state_dict['updated_at']), str)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.state.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.state.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method"""
        self.state.name = "California"
        string = str(self.state)
        self.assertIn("[State]", string)
        self.assertIn("'name': 'California'", string)

    def test_save_method(self):
        """Test save method"""
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)

    def test_kwargs(self):
        """Test creating instance with kwargs"""
        state_dict = self.state.to_dict()
        new_state = State(**state_dict)
        self.assertEqual(self.state.id, new_state.id)
        self.assertEqual(self.state.created_at, new_state.created_at)
        self.assertEqual(self.state.updated_at, new_state.updated_at)
        self.assertNotEqual(self.state, new_state)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test the save method"""
        self.state.save()
        self.assertTrue(mock_storage.save.called)

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test that new is called in init"""
        state = State()
        self.assertTrue(mock_storage.new.called)


if __name__ == "__main__":
    unittest.main()
