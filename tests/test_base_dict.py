#!/usr/bin/python3

import unittest
from models.base_model import BaseModel
from datetime import datetime
import os
import models
from time import sleep


class TestBaseModelToDictMethod(unittest.TestCase):
    """Test cases for the to_dict method of the BaseModel class."""
    def setUp(self):
        """Set up the test environment by creating a BaseModel instance."""
        self.base_model = BaseModel()

    def test_to_dict_return_type(self):
        """
        Test the return type of the to_dict method.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        self.assertIsInstance(dict_data, dict)

    def test_to_dict_has_class_key(self):
        """
        Test if the 'to_dict' dictionary contains the '__class__' key.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        self.assertIn('__class__', dict_data)

    def test_to_dict_class_key_value(self):
        """
        Test the value of the '__class__' key in the 'to_dict' dictionary.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        self.assertEqual(dict_data['__class__'], 'BaseModel')

    def test_to_dict_contains_created_at(self):
        """
        Test if the 'to_dict' dictionary contains the 'created_at' key.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        self.assertIn('created_at', dict_data)

    def test_to_dict_contains_updated_at(self):
        """
        Test if the 'to_dict' dictionary contains the 'updated_at' key.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        self.assertIn('updated_at', dict_data)

    def test_to_dict_created_at_format(self):
        """
        Test the format of the 'created_at' attribute in the 'to_dict' dictionary.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        datetime_format = '%Y-%m-%dT%H:%M:%S.%f'
        date_str = dict_data['created_at']
        self.assertTrue(datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f'))

    def test_to_dict_updated_at_format(self):
        """
        Test the format of the 'updated_at' attribute in the 'to_dict' dictionary.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        date_str = dict_data['updated_at']
        self.assertTrue(datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%S.%f'))

    def test_to_dict_contains_id(self):
        """
        Test if the 'to_dict' dictionary contains the 'id' key.

        Returns:
            None
        """
        dict_data = self.base_model.to_dict()
        self.assertIn('id', dict_data)

    def test_to_dict_contains_additional_attrs(self):
        """
        Test if the 'to_dict' dictionary contains additional attributes.

        Returns:
            None
        """
        self.base_model.name = "Test Name"
        self.base_model.number = 42
        dict_data = self.base_model.to_dict()
        self.assertIn('name', dict_data)
        self.assertIn('number', dict_data)


if __name__ == '__main__':
    unittest.main()
