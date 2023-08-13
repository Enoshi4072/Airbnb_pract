import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import models
import os


class TestBaseModel(unittest.TestCase):

    def test_instance_attributes(self):
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))

    def test_default_attributes(self):
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_custom_attributes(self):
        data = {
            'id': '123',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-01T12:30:00.000000',
            'name': 'test'
        }
        instance = BaseModel(**data)
        self.assertEqual(instance.id, '123')
        self.assertEqual(instance.name, 'test')
        self.assertEqual(instance.created_at, datetime(2023, 1, 1, 12, 0, 0))
        self.assertEqual(instance.updated_at, datetime(2023, 1, 1, 12, 30, 0))

    def test_save_method(self):
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_to_dict_method(self):
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')

    def test_new_method(self):
        instance = BaseModel()
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.assertIn(key, storage.all())

    def test_init_with_kwargs(self):
        data = {
            'id': '123',
            'created_at': '2023-01-01T12:00:00.000000',
            'updated_at': '2023-01-01T12:30:00.000000',
            'name': 'test'
        }
        instance = BaseModel(**data)
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.assertIn(key, storage.all())

if __name__ == '__main__':
    unittest.main()

