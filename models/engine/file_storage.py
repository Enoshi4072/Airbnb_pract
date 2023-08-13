#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    A class to handle serialization and deserialization
    of objects to/from JSON format.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects.

        Returns:
            dict: A dictionary containing objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the __objects dictionary.

        Args:
            obj (BaseModel): The object to be added.
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes objects to JSON and saves them to the file.
        """
        data = {}
        for key, value in FileStorage.__objects.items():
            data[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding="utf-8") as f:
            json.dump(data, f)

    def reload(self):
        """
        Deserializes JSON data from the file and creates objects.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name = value['__class__']
                    obj = eval(class_name)(**value)
                    self.new(obj)
