#!/usr/bin/python3
"""Test script for testing the Amenity Class"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def setUp(self):
        """Set up the test environment"""
        self.amenity = Amenity()

    def tearDown(self):
        """Clean up after each test"""
        del self.amenity

    def test_is_instance(self):
        """Test if amenity is an instance of BaseModel"""
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """Test the attributes of Amenity"""
        self.assertEqual(self.amenity.name, "")

    def test_to_dict(self):
        """Test to_dict method"""
        amenity_dict = self.amenity.to_dict()
        self.assertEqual(amenity_dict['__class__'], 'Amenity')
        self.assertEqual(type(amenity_dict['created_at']), str)
        self.assertEqual(type(amenity_dict['updated_at']), str)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.amenity.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.amenity.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method"""
        self.amenity.name = "Pool"
        string = str(self.amenity)
        self.assertIn("[Amenity]", string)
        self.assertIn("'name': 'Pool'", string)

    def test_save_method(self):
        """Test save method"""
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
