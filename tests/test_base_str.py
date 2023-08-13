#!/usr/bin/python3

import os
import models
from datetime import datetime
from datetime import time
import unittest
from models.base_model import BaseModel


class TestBaseModelStrMethod(unittest.TestCase):
    """Test cases for the __str__ method of the BaseModel class."""
    def setUp(self):
        """Set up a BaseModel instance for testing."""
        self.base_model = BaseModel()

    def test_str_with_default_instance(self):
        """Test the __str__ method with a default instance."""
        e = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), e)

    def test_str_with_attributes(self):
        """Test the __str__ method with additional attributes."""
        self.base_model.name = "Test Name"
        self.base_model.number = 42
        e = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), e)

    def test_str_output_type(self):
        """Test the output type of the __str__ method."""
        self.assertIsInstance(str(self.base_model), str)

    def test_str_after_update(self):
        """Test __str__ method after updating an attribute."""
        initial = str(self.base_model)
        self.base_model.name = "Updated Name"
        updated = str(self.base_model)
        self.assertNotEqual(initial, updated)

    def test_str_after_delete(self):
        """Test __str__ method with special characters in attributes."""
        self.base_model.name = "Test Name"
        initial = str(self.base_model)
        del self.base_model.name
        updated = str(self.base_model)
        self.assertNotEqual(initial, updated)

    def test_str_with_special_characters(self):
        """Test the __str__ method with
        attributes containing special characters."""
        self.base_model.special = "!@#$%^&*()"
        e = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), e)

    def test_str_with_multiple_attributes(self):
        """Test the __str__ method with multiple attributes."""
        self.base_model.attr1 = "value1"
        self.base_model.attr2 = "value2"
        e = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), e)

    def test_str_with_datetime_attributes(self):
        """Test the __str__ method with datetime attributes."""
        self.base_model.created_at = "2023-08-15T12:00:00.000000"
        self.base_model.updated_at = "2023-08-15T12:30:00.000000"
        e = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), e)

    def test_str_with_non_string_attributes(self):
        """Test the __str__ method with non-string attributes."""
        self.base_model.number = 42
        self.base_model.boolean = True
        e = f"[BaseModel] ({self.base_model.id}) {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), e)


if __name__ == '__main__':
    unittest.main()
