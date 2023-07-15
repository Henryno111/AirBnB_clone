#!/usr/bin/python3
"""define a new class that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represnt the user class
    
    Attributes:
            email(str): empty string
            password(str): empty string
            first_name(str): empty string
            last_name(str): empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
