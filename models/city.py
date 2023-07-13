#!/usr/bin/python3
"""define a new class that inherits from BaseModel"""
from models.base_model import BaseModel


class City(BaseModel):
    """represnt the city class
    Attributes:
         state_id(str): empty string
         name(str): empty string
    """
    state_id = ""
    name = ""
