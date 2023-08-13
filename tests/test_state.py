#!/usr/bin/python3

import os
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from datetime import datetime
import unittest
from models.state import State
from time import sleep


class TestState(unittest.TestCase):
    def test_name_is_public_class_attribute(self):
        """
        Test if 'name' is a public class attribute.
        """
        self.assertEqual(str, type(State.name))

    def test_state_instance_creation(self):
        """
        Test if a State instance is properly created.
        """
        state = State()
        self.assertIsInstance(state, State)

    def test_state_name_attribute(self):
        """
        Test if State instance has 'name' as an attribute.
        """
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_state_id_attribute(self):
        """
        Test if State instance has 'id' as an attribute.
        """
        state = State()
        self.assertTrue(hasattr(state, 'id'))

    def test_state_created_at_attribute(self):
        """
        Test if State instance has 'created_at' as an attribute.
        """
        state = State()
        self.assertTrue(hasattr(state, 'created_at'))

    def test_state_updated_at_attribute(self):
        """
        Test if State instance has 'updated_at' as an attribute.
        """
        state = State()
        self.assertTrue(hasattr(state, 'updated_at'))

    def test_state_to_dict_method(self):
        """
        Test if 'to_dict' method returns a dictionary
        representation of the State instance.
        """
        state = State()
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)

    def test_state_str_method(self):
        """
        Test if '__str__' method returns a string
        representation of the State instance.
        """
        state = State()
        state_str = str(state)
        self.assertIsInstance(state_str, str)

    def test_save_with_arg(self):
        state = State()
        with self.assertRaises(TypeError):
            state.save(None)


if __name__ == '__main__':
    unittest.main()
