#!/usr/bin/python3

import os
import json
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review
from unittest.mock import patch, mock_open


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        self.storage = FileStorage()

    def test_FileStorage_instantiation_with_arg(self):
        """Test if instantiation with an argument raises TypeError."""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        """Test if '__file_path' attribute is a private string."""
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def test_FileStorage_objects_is_private_dict(self):
        """Test if '__objects' attribute is a private dictionary."""
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_all_method_returns_dict(self):
        """Test if 'all' method returns a dictionary."""
        result = FileStorage().all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_object(self):
        """Test if 'new' adds object to '__objects'."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, storage._FileStorage__objects)

    def test_new_method_adds_correct_key(self):
        """Test if 'new' adds correct key to '__objects'."""
        storage = FileStorage()
        obj = BaseModel()
        storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertEqual(obj, storage._FileStorage__objects[key])

    def test_new_adds_object_to_objects(self):
        """
        Test if new method adds a BaseModel object to __objects.

        It ensures that a BaseModel object is correctly added to the
        '__objects' attribute of the FileStorage
        class when using the new method.
        """
        storage = FileStorage()
        bm = BaseModel()
        storage.new(bm)
        key = "BaseModel." + bm.id
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key], bm)

    def test_new_adds_user_to_objects(self):
        """
        Test if new method adds a User object to __objects.

        It ensures that a User object is correctly added to the
        '__objects' attribute of the FileStorage
        class when using the new method.
        """
        storage = FileStorage()
        user = User()
        storage.new(user)
        key = "User." + user.id
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key], user)

    def test_new_with_invalid_arg(self):
        """
        Test if new method raises AttributeError with invalid argument.

        It ensures that the new method raises an AttributeError when trying to
        add an invalid argument (None) to the '__objects' attribute of the
        FileStorage class.
        """
        storage = FileStorage()
        with self.assertRaises(AttributeError):
            storage.new(None)

    def test_new_adds_multiple_objects(self):
        """
        Test if new method adds multiple BaseModel objects to __objects.

        It ensures that multiple BaseModel objects are correctly added to the
        '__objects' attribute of the FileStorage
        class when using the new method.
        """
        storage = FileStorage()
        bm1 = BaseModel()
        bm2 = BaseModel()
        storage.new(bm1)
        storage.new(bm2)
        key1 = "BaseModel." + bm1.id
        key2 = "BaseModel." + bm2.id
        self.assertIn(key1, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key1], bm1)
        self.assertIn(key2, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key2], bm2)

    def test_new_adds_city_to_objects(self):
        """
        Test if new method adds a City object to __objects.

        It ensures that a City object is correctly added to the
        '__objects' attribute of the FileStorage
        class when using the new method.
        """
        storage = FileStorage()
        city = City()
        storage.new(city)
        key = "City." + city.id
        self.assertIn(key, storage._FileStorage__objects)
        self.assertIs(storage._FileStorage__objects[key], city)

    def test_save_with_arg(self):
        """
        Test if save method raises TypeError with invalid argument.

        It ensures that the save method raises a TypeError when trying to
        call it with an invalid argument (None).
        """
        storage = FileStorage()
        with self.assertRaises(TypeError):
            storage.save(None)

    def test_reload_with_arg(self):
        """
        Test if reload method raises TypeError with invalid argument.

        It ensures that the reload method raises a TypeError when trying to
        call it with an invalid argument (None)
        through the models.storage object.
        """
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == '__main__':
    unittest.main()
