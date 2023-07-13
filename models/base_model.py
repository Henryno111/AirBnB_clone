#!/usr/bin/python3
"""Define a new class called BaseModel"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """Represent BaseModel class"""

    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel
        
        Args:
            *args(any): unused
            **kwargs(dict): key/value ot attributes
        """
        formtime = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, formtime)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)
                   
    
    def save(self):
        """update a public attribute"""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """return a dictionary containing all attributes already fixed"""
        dictrepr = self.__dict__.copy()
        dictrepr["created_at"] = self.created_at.isoformat()
        dictrepr["updated_at"] = self.updated_at.isoformat()
        dictrepr["__class__"] = self.__class__.__name__
        return (dictrepr)

    def __str__(self):
        """ represent the instance of this class"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
