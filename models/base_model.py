#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """
    BaseModel class for the AirBnB clone project.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): The datetime when the instance was created.
        updated_at (datetime): The datetime when the instance was last updated.
    """
    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                format_string = '%Y-%m-%dT%H:%M:%S.%f'
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, format_string))
                else:
                    setattr(self, key, value)
        else:
            models.storage.new(self)

    def save(self):
        """
        Updates the updated_at attribute with
        the current datetime and saves the instance.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Converts the instance attributes to a dictionary representation.

        Returns:
            dict: A dictionary containing the instance attributes.
        """
        data = self.__dict__.copy()
        data['__class__'] = self.__class__.__name__
        data['created_at'] = self.created_at.isoformat()
        data['updated_at'] = self.updated_at.isoformat()
        return data

    def __str__(self):
        """
        Returns a string representation of the instance.

        Returns:
            str: A formatted string representing the instance.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )
