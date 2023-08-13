#!/usr/bin/python3

import unittest
import models
import os
from datetime import datetime
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def test_place_id_is_public_class_attribute(self):
        """Test if 'place_id' is a public class attribute."""
        self.assertEqual(str, type(Review.place_id))

    def test_user_id_is_public_class_attribute(self):
        """Test if 'user_id' is a public class attribute."""
        self.assertEqual(str, type(Review.user_id))

    def test_text_is_public_class_attribute(self):
        """Test if 'text' is a public class attribute."""
        self.assertEqual(str, type(Review.text))

    def test_instantiation(self):
        """Test if Review instance can be created."""
        review = Review()
        self.assertIsInstance(review, Review)

    def test_instantiation_with_attributes(self):
        """Test if Review instance can be created with attributes."""
        review = Review(place_id="123", user_id="456", text="Great place!")
        self.assertEqual(review.place_id, "123")
        self.assertEqual(review.user_id, "456")
        self.assertEqual(review.text, "Great place!")

    def test_str_method(self):
        """Test the __str__ method."""
        review = Review()
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        review = Review(place_id="123", user_id="456", text="Great place!")
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], "Review")
        self.assertEqual(review_dict['place_id'], "123")
        self.assertEqual(review_dict['user_id'], "456")
        self.assertEqual(review_dict['text'], "Great place!")
        self.assertIn('id', review_dict)
        self.assertIn('created_at', review_dict)
        self.assertIn('updated_at', review_dict)

    def test_to_dict_created_at_updated_at_types(self):
        """Test types of 'created_at' and 'updated_at' in to_dict."""
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(str, type(review_dict['created_at']))
        self.assertEqual(str, type(review_dict['updated_at']))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance is stored in the objects dictionary."""
        review = Review()
        self.assertIn(review, models.storage.all().values())

    def test_two_reviews_unique_ids(self):
        """Test if two Review instances have unique IDs."""
        review1 = Review()
        review2 = Review()
        self.assertNotEqual(review1.id, review2.id)


if __name__ == '__main__':
    unittest.main()
