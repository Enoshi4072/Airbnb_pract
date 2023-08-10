#!/usr/bin/python3

import json
from os.path import exists

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        data = {}
        for key, value in self.__objects.items():
            data[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f)

    def reload(self):
        if exists(self.__file_path):
            with open(self.__file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    cls_name, obj_id = key.split('.')
                    cls = eval(cls_name)
                    self.__objects[key] = cls(**value)
