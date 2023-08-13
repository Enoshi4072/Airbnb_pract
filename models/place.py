#!/usr/bin/python3

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel.

    Attributes:
        city_id (str): The ID of the City to which the Place belongs.
        user_id (str): The ID of the User who owns the Place.
        name (str): The name of the Place.
        description (str): A description of the Place.
        number_rooms (int): The number of rooms in the Place.
        number_bathrooms (int): The number of bathrooms in the Place.
        max_guest (int): The max num of guests the Place can accommodate.`
        price_by_night (int): The price of the Place per night.
        latitude (float): The latitude coordinates of the Place's location.
        longitude (float): The longitude coordinates of the Place's location.
        amenity_ids (list): A list of Amenity IDs associated with the Place.
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
