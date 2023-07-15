#!/usr/bin/python3
"""define a new class that inherits from BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """represent the amenity class
    
    Attributes:
          name(str): empty string
    """

    name = ""
