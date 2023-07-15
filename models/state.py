#!/usr/bin/python3
"""define a new class that inherits from BaseModel"""
from models.base_model import BaseModel


class State(BaseModel):
    """represent the state class

    Attributes:
           name(str): empty string
    """

    name = ""
