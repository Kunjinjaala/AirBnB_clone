#!/usr/bin/python3
"""Test script for testing the City Class"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestCity(unittest.TestCase):
    """Test the City class"""

    def setUp(self):
        """Set up the test environment"""
        self.city = City()

    def tearDown(self):
        """Clean up after each test"""
        del self.city

    def test_is_instance(self):
        """Test if city is an instance of BaseModel"""
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """Test the attributes of City"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        city_dict = self.city.to_dict()
        self.assertEqual(city_dict['__class__'], 'City')
        self.assertEqual(type(city_dict['created_at']), str)
        self.assertEqual(type(city_dict['updated_at']), str)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.city.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.city.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method"""
        self.city.name = "San Francisco"
        string = str(self.city)
        self.assertIn("[City]", string)
        self.assertIn("'name': 'San Francisco'", string)

    def test_save_method(self):
        """Test save method"""
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)

    def test_kwargs(self):
        """Test creating instance with kwargs"""
        city_dict = self.city.to_dict()
        new_city = City(**city_dict)
        self.assertEqual(self.city.id, new_city.id)
        self.assertEqual(self.city.created_at, new_city.created_at)
        self.assertEqual(self.city.updated_at, new_city.updated_at)
        self.assertNotEqual(self.city, new_city)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test the save method"""
        self.city.save()
        self.assertTrue(mock_storage.save.called)

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test that new is called in init"""
        city = City()
        self.assertTrue(mock_storage.new.called)


if __name__ == "__main__":
    unittest.main()
