#!/usr/bin/python3

import models
import unittest
from models.base_model import BaseModel
from models import storage
from datetime import datetime
from time import sleep


class TestBaseModelSaveMethod(unittest.TestCase):
    """Test cases for the save method of the BaseModel class."""
    def setUp(self):
        """Set up the test environment with a BaseModel instance."""
        self.base_model = BaseModel()

    def test_save_updates_updated_at(self):
        """Test if 'save' method updates 'updated_at' attribute."""
        prev_updated = self.base_model.updated_at
        self.base_model.save()
        self.assertNotEqual(prev_updated, self.base_model.updated_at)

    def test_save_updates_file_storage(self):
        """Test if 'save' method updates object in FileStorage."""
        initial_updated = self.base_model.updated_at
        sleep(0.01)  # Sleep to create a time difference
        self.base_model.save()
        obj_k = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        updated = models.storage.all()[obj_k]
        self.assertNotEqual(initial_updated, updated.updated_at)

    def test_save_updates_file_content(self):
        """Test if 'save' method updates object in file content."""
        initial_updated = self.base_model.updated_at
        self.base_model.save()
        storage.reload()
        obj_k = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        updated = models.storage.all()[obj_k]
        self.assertNotEqual(initial_updated, updated.updated_at)

    def test_save_method_returns_none(self):
        """Test if 'save' method returns None."""
        self.assertIsNone(self.base_model.save())

    def test_save_method_updates_created_at(self):
        """Test if 'save' method updates 'created_at' attribute."""
        initial_created = self.base_model.created_at
        self.base_model.save()
        obj_k = f"{self.base_model.__class__.__name__}.{self.base_model.id}"
        updated = models.storage.all()[obj_k]
        self.assertEqual(initial_created, updated.created_at)

    def test_save_does_not_add_new_object(self):
        """Test if 'save' method does not add a new object to storage."""
        count_before = len(storage.all())
        self.base_model.save()
        count_after = len(storage.all())
        self.assertEqual(count_before, count_after)

    def test_save_updates_all_instances(self):
        """Test if 'save' method updates 'updated_at' for all instances."""
        bm1 = BaseModel()
        bm2 = BaseModel()
        bm1.save()
        bm2.save()
        updated_bm1 = storage.all()[f"{bm1.__class__.__name__}.{bm1.id}"]
        updated_bm2 = storage.all()[f"{bm2.__class__.__name__}.{bm2.id}"]
        self.assertEqual(bm1.updated_at, updated_bm1.updated_at)
        self.assertEqual(bm2.updated_at, updated_bm2.updated_at)


if __name__ == '__main__':
    unittest.main()
