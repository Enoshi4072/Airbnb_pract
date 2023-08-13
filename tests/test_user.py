#!/usr/bin/python3

import models
import os
import unittest
from models.base_model import BaseModel
from datetime import datetime
from models.user import User
import models


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def test_email_is_public_class_attribute(self):
        """Test if 'email' is a public class attribute."""
        self.assertEqual(str, type(User.email))

    def test_password_is_public_class_attribute(self):
        """Test if 'password' is a public class attribute."""
        self.assertEqual(str, type(User.password))

    def test_first_name_is_public_class_attribute(self):
        """Test if 'first_name' is a public class attribute."""
        self.assertEqual(str, type(User.first_name))

    def test_last_name_is_public_class_attribute(self):
        """Test if 'last_name' is a public class attribute."""
        self.assertEqual(str, type(User.last_name))

    def test_instantiation(self):
        """Test if User instance can be created."""
        user = User()
        self.assertIsInstance(user, User)

    def test_instantiation_with_attributes(self):
        """Test if User instance can be created with attributes."""
        user = User(email="test@example.com", password="secure",
                    first_name="John", last_name="Doe")
        self.assertEqual(user.email, "test@example.com")
        self.assertEqual(user.password, "secure")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")

    def test_str_method(self):
        """Test the __str__ method."""
        user = User()
        expected_str = "[User] ({}) {}".format(user.id, user.__dict__)
        self.assertEqual(str(user), expected_str)

    def test_to_dict_method(self):
        """Test the to_dict method."""
        user = User(email="test@example.com", password="secure",
                    first_name="John", last_name="Doe")
        user_dict = user.to_dict()
        self.assertEqual(user_dict['__class__'], "User")
        self.assertEqual(user_dict['email'], "test@example.com")
        self.assertEqual(user_dict['password'], "secure")
        self.assertEqual(user_dict['first_name'], "John")
        self.assertEqual(user_dict['last_name'], "Doe")
        self.assertIn('id', user_dict)
        self.assertIn('created_at', user_dict)
        self.assertIn('updated_at', user_dict)

    def test_to_dict_created_at_updated_at_types(self):
        """Test types of 'created_at' and 'updated_at' in to_dict."""
        user = User()
        user_dict = user.to_dict()
        self.assertEqual(str, type(user_dict['created_at']))
        self.assertEqual(str, type(user_dict['updated_at']))

    def test_new_instance_stored_in_objects(self):
        """Test if a new instance is stored in the objects dictionary."""
        user = User()
        self.assertIn(user, models.storage.all().values())

    def test_two_users_unique_ids(self):
        """Test if two User instances have unique IDs."""
        user1 = User()
        user2 = User()
        self.assertNotEqual(user1.id, user2.id)

    def test_instantiation_with_kwargs(self):
        dt = datetime.today()
        dt_iso = dt.isoformat()
        us = User(id="400", created_at=dt_iso, updated_at=dt_iso)
        self.assertEqual(us.id, "400")
        self.assertEqual(us.created_at, dt)
        self.assertEqual(us.updated_at, dt)


if __name__ == '__main__':
    unittest.main()
