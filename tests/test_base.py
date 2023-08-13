import unittest
from datetime import datetime
from models.base_model import BaseModel
from models import storage
import models
import os
from time import sleep


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.
    """

    def test_instance_attributes(self):
        """
        Test the presence of instance attributes.
        """
        instance = BaseModel()
        self.assertTrue(hasattr(instance, 'id'))
        self.assertTrue(hasattr(instance, 'created_at'))
        self.assertTrue(hasattr(instance, 'updated_at'))

    def test_default_attributes(self):
        """
        Test the default data types of attributes.
        """
        instance = BaseModel()
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime)
        self.assertIsInstance(instance.updated_at, datetime)

    def test_id_is_public_str(self):
        """
        Test if the 'id' attribute is of type string.
        """
        new_instance = BaseModel()
        self.assertEqual(str, type(new_instance.id))

    def test_custom_attributes(self):
        """
        Test initialization with custom attribute values.
        """
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

    def test_no_args_instantiates(self):
        """
        Test if BaseModel instantiation without arguments works.
        """
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_instantiation_with_args_and_kwargs(self):
        """
        Test instantiation with positional and keyword arguments.
        """
        dt = datetime.today()
        dt_iso = dt.isoformat()
        bm = BaseModel("12", id="345", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(bm.id, "345")
        self.assertEqual(bm.created_at, dt)
        self.assertEqual(bm.updated_at, dt)

    def test_two_models_different_created_at(self):
        """
        Test if two instances have different 'created_at' attributes.
        """
        bm1 = BaseModel()
        sleep(0.05)
        bm2 = BaseModel()
        self.assertLess(bm1.created_at, bm2.created_at)

    def test_two_models_unique_ids(self):
        """
        Test if two instances have unique IDs.
        """
        bm1 = BaseModel()
        bm2 = BaseModel()
        self.assertNotEqual(bm1.id, bm2.id)

    def test_updated_at_is_public_datetime(self):
        """
        Test if 'updated_at' attribute is of type datetime.
        """
        new_instance = BaseModel()
        self.assertEqual(datetime, type(new_instance.updated_at))

    def test_created_at_is_public_datetime(self):
        """
        Test if 'created_at' attribute is of type datetime.
        """
        new_instance = BaseModel()
        self.assertEqual(datetime, type(new_instance.created_at))

    def test_save_method(self):
        """
        Test the save method to update the 'updated_at' attribute.
        """
        instance = BaseModel()
        initial_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(initial_updated_at, instance.updated_at)

    def test_new_instance_stored_in_objects(self):
        """
        Test if a new instance is stored in the objects dictionary.
        """
        new_instance = BaseModel()
        self.assertIn(new_instance, models.storage.all().values())

    def test_to_dict_method(self):
        """
        Test the to_dict method of the BaseModel class.
        """
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn('id', instance_dict)
        self.assertIn('created_at', instance_dict)
        self.assertIn('updated_at', instance_dict)
        self.assertEqual(instance_dict['__class__'], 'BaseModel')

    def test_new_method(self):
        """
        Test the new method of the BaseModel class.
        """
        instance = BaseModel()
        key = "{}.{}".format(instance.__class__.__name__, instance.id)
        self.assertIn(key, storage.all())


if __name__ == '__main__':
    unittest.main()
