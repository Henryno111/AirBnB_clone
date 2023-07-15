#!/usr/bin/python3
"""define a new class that inherits from BaseModel"""
from models.base_model import BaseModel


class Review(BaseModel):
    """represent the review class
    
    Attributes:
        place_id(str): empty string
        user_id(str): empty string
        text(str): empty string
    """

    place_id = ""
    user = ""
    text = ""
