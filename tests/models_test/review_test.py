#!/usr/bin/python3
"""Test script for testing the Review Class"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime

class TestReview(unittest.TestCase):
    """Test the Review class"""

    def setUp(self):
        """Set up the test environment"""
        self.review = Review()

    def tearDown(self):
        """Clean up after each test"""
        del self.review

    def test_is_instance(self):
        """Test if review is an instance of BaseModel"""
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """Test the attributes of Review"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_to_dict(self):
        """Test to_dict method"""
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)

    def test_created_at(self):
        """Test created_at attribute"""
        self.assertIsInstance(self.review.created_at, datetime)

    def test_updated_at(self):
        """Test updated_at attribute"""
        self.assertIsInstance(self.review.updated_at, datetime)

    def test_str_method(self):
        """Test __str__ method"""
        self.review.text = "Great place!"
        string = str(self.review)
        self.assertIn("[Review]", string)
        self.assertIn("'text': 'Great place!'", string)

    def test_save_method(self):
        """Test save method"""
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
