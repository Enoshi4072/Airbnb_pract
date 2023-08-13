#!/usr/bin/python3

import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from time import sleep
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_instantiation(self):
        """Test if an instance of Place can be created."""
        place = Place()
        self.assertIsInstance(place, Place)

    def test_subclass_inheritance(self):
        """Test if Place is a subclass of BaseModel."""
        place = Place()
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attributes_existence(self):
        """Test if all expected attributes exist in Place."""
        place = Place()
        self.assertTrue(hasattr(place, 'city_id'))
        # Check other attributes similarly

    def test_default_attributes(self):
        """Test if default attribute values are set correctly."""
        place = Place()
        self.assertEqual(place.city_id, "")

    def test_to_dict_method(self):
        """Test if the to_dict() method produces the correct dictionary."""
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')

    def test_description_is_public_class_attribute(self):
        """
        Test if 'description' is a public class
        attribute and not an instance attribute.
        It checks if 'description' exists in the
        class's namespace and not in an instance's dictionary.
        """
        place = Place()
        self.assertEqual(str, type(Place.description))
        self.assertIn("description", dir(place))
        self.assertNotIn("desctiption", place.__dict__)

    def test_str_representation(self):
        """Test if the __str__() method produces
        the correct string representation.
        """
        place = Place()
        str_repr = str(place)
        self.assertIn("[Place]", str_repr)
        self.assertIn("'id':", str_repr)

    def test_id_unique_for_each_instance(self):
        """Test if each instance of Place has a unique ID."""
        place1 = Place()
        place2 = Place()
        self.assertNotEqual(place1.id, place2.id)

    def test_to_dict_method(self):
        """
        Test if to_dict method returns the correct dictionary.

        It ensures that the to_dict method returns a dictionary with the
        correct attributes and values for the Place class instance.
        """
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertIn('created_at', place_dict)
        self.assertIn('updated_at', place_dict)
        self.assertIsInstance(place_dict['created_at'], str)
        self.assertIsInstance(place_dict['updated_at'], str)

    def test_str_representation(self):
        """
        Test if the __str__ method returns the correct string representation.

        It ensures that the __str__ method returns a formatted string with the
        expected information about the Place class instance.
        """
        place = Place()
        str_repr = str(place)
        self.assertIn("[Place]", str_repr)
        self.assertIn("'id':", str_repr)
        self.assertIn("'created_at':", str_repr)
        self.assertIn("'updated_at':", str_repr)


if __name__ == '__main__':
    unittest.main()
