#!/usr/bin/python3
"""define a new class that inherits from BaseModel"""
from models.base_model import BaseModel


class Place(BaseModel):
    """represent the place class

    Attributes:
        city_id(str): empty string
        user_id(str): empty strig
        name(str): empty string
        description(str): empty string
        number_rooms(int): integer
        number_bathrooms(int): integer
        max_guest(int): integer
        price_by_night(int): integer
        latitude(float): float
        longitude(float): float
        amenity_ids(list): empty list
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
