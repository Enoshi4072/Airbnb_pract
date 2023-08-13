#!/usr/bin/python3

from datetime import datetime
from models.base_model import BaseModel
import models
import os
import unittest
import json
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        self.storage = FileStorage()

    def test_file_path_attribute_exists(self):
        """Test if '__file_path' attribute exists."""
        self.assertIn("__file_path", dir(self.storage))

    def test_objects_attribute_exists(self):
        """Test if '__objects' attribute exists."""
        self.assertIn("__objects", dir(self.storage))

    def test_all_method_returns_dict(self):
        """Test if 'all' method returns a dictionary."""
        result = self.storage.all()
        self.assertIsInstance(result, dict)

    def test_new_method_adds_to_objects(self):
        """Test if 'new' method adds object to '__objects'."""
        obj = BaseModel()
        self.storage.new(obj)
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.assertIn(key, self.storage.__objects)

    def test_save_method_creates_file(self):
        """Test if 'save' method creates a file."""
        self.storage.save()
        self.assertTrue(os.path.exists(self.storage.__file_path))

    def test_save_method_updates_file(self):
        """Test if 'save' method updates the file content."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()

        with open(self.storage.__file_path, 'r') as f:
            data = json.load(f)
            self.assertIn(key, data)

    def test_reload_method_loads_objects(self):
        """Test if 'reload' method loads objects from file."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        self.assertIn(key, self.storage.__objects)

    def test_reload_method_updates_objects(self):
        """Test if 'reload' method updates objects from file."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        obj_copy = self.storage.__objects[key]
        self.assertEqual(obj.to_dict(), obj_copy.to_dict())

    def test_reload_method_updates_created_at(self):
        """Test if 'reload' method updates 'created_at' attribute."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        obj_copy = self.storage.__objects[key]
        self.assertEqual(obj.created_at, obj_copy.created_at)

    def test_reload_method_updates_updated_at(self):
        """Test if 'reload' method updates 'updated_at' attribute."""
        obj = BaseModel()
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        obj_copy = self.storage.__objects[key]
        self.assertEqual(obj.updated_at, obj_copy.updated_at)

    def test_reload_method_updates_objects_count(self):
        """Test if 'reload' method updates '__objects' count."""
        initial_count = len(self.storage.__objects)
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        updated_count = len(self.storage.__objects)
        self.assertEqual(initial_count + 1, updated_count)

    def test_reload_method_updates_objects_attributes(self):
        """Test if 'reload' method updates object attributes."""
        obj = BaseModel()
        obj.foo = "bar"
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.storage.new(obj)
        self.storage.save()
        self.storage.reload()
        obj_copy = self.storage.__objects[key]
        self.assertEqual(obj.foo, obj_copy.foo)

if __name__ == '__main__':
    unittest.main()
