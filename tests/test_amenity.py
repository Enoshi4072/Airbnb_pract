#!/usr/bin/python3

from models.base_model import BaseModel
import unittest
from models.amenity import Amenity
import os
from time import sleep
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def test_amenity_inherits_base_model(self):
        """Test if Amenity inherits from BaseModel."""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)

    def test_amenity_has_name_attribute(self):
        """Test if Amenity class has the 'name' attribute."""
        self.assertTrue(hasattr(Amenity, 'name'))

    def test_amenity_name_defaults_to_empty_string(self):
        """Test the default value of the 'name' attribute."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_assign_value_to_amenity_name(self):
        """Test assignment of value to the 'name' attribute."""
        amenity = Amenity(name="Swimming Pool")
        self.assertEqual(amenity.name, "Swimming Pool")

    def test_amenity_to_dict_method(self):
        """Test the to_dict method of the Amenity class."""
        amenity = Amenity(name="Gym")
        amenity_dict = amenity.to_dict()
        expected_keys = ['id', 'created_at', 'updated_at', 'name', '__class__']
        self.assertTrue(all(key in amenity_dict for key in expected_keys))

    def test_amenity_str_representation(self):
        """Test the __str__ method of the Amenity class."""
        amenity = Amenity(name="Sauna")
        expected_str = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(str(amenity), expected_str)

    def test_amenity_created_at_is_datetime(self):
        """Test if 'created_at' attribute is a datetime instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity.created_at, datetime)

    def test_amenity_updated_at_is_datetime(self):
        """Test if 'updated_at' attribute is a datetime instance."""
        amenity = Amenity()
        self.assertIsInstance(amenity.updated_at, datetime)

    def test_amenity_save_method_updates_updated_at(self):
        """Test if 'save' method updates 'updated_at' attribute."""
        amenity = Amenity()
        original_updated_at = amenity.updated_at
        amenity.save()
        self.assertNotEqual(original_updated_at, amenity.updated_at)

    def test_amenity_id_is_str(self):
        """Test if 'id' attribute is of type string."""
        amenity = Amenity()
        self.assertEqual(str, type(amenity.id))

    def test_amenity_created_at_is_datetime(self):
        """Test if 'created_at' attribute is of type datetime."""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.created_at))

    def test_amenity_updated_at_is_datetime(self):
        """Test if 'updated_at' attribute is of type datetime."""
        amenity = Amenity()
        self.assertEqual(datetime, type(amenity.updated_at))

    def test_two_amenities_unique_ids(self):
        """Test if two instances of Amenity have unique ids."""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

if __name__ == '__main__':
    unittest.main()
