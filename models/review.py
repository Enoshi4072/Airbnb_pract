#!/usr/bin/python3

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel.

    Attributes:
        place_id (str): The ID of the associated Place.
        user_id (str): The ID of the associated User.
        text (str): The text content of the review.
    """
    place_id = ""
    user_id = ""
    text = ""
