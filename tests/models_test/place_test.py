#!/usr/bin/python3
"""Test script for testing the Place Class"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime
from unittest.mock import patch


class TestPlace(unittest.TestCase):
    """Test the Place class"""

    def setUp(self):
        """Set up the test environment"""
        self.place = Place()

    def tearDown(self):
        """Clean up after each test"""
        del self.place

    def test_is_instance(self):
        """Test if place is an instance of BaseModel"""
        self.assertIsInstance(self.place, BaseModel)

    def test_attributes(self):
        """Test the attributes of Place"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_to_dict(self):
        """Test to_dict method"""
        place_dict = self.place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(type(place_dict['created_at']), str)
        self.assertEqual(type(place_dict['updated_at']), str)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.place.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.place.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method"""
        self.place.name = "Beach House"
        string = str(self.place)
        self.assertIn("[Place]", string)
        self.assertIn("'name': 'Beach House'", string)

    def test_save_method(self):
        """Test save method"""
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)

    def test_kwargs(self):
        """Test creating instance with kwargs"""
        place_dict = self.place.to_dict()
        new_place = Place(**place_dict)
        self.assertEqual(self.place.id, new_place.id)
        self.assertEqual(self.place.created_at, new_place.created_at)
        self.assertEqual(self.place.updated_at, new_place.updated_at)
        self.assertNotEqual(self.place, new_place)

    @patch('models.storage')
    def test_save(self, mock_storage):
        """Test the save method"""
        self.place.save()
        self.assertTrue(mock_storage.save.called)

    @patch('models.storage')
    def test_new(self, mock_storage):
        """Test that new is called in init"""
        place = Place()
        self.assertTrue(mock_storage.new.called)


if __name__ == "__main__":
    unittest.main()
