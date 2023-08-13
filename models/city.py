#!/usr/bin/python3

from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that inherits from BaseModel.

    Attributes:
        state_id (str): The ID of the associated State.
        name (str): The name of the City.
    """
    state_id = ""
    name = ""
