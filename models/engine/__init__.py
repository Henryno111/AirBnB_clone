#!/usr/bin/python3
"""Define a new class called FileStorage"""
import json
from models.base_model import BaseModel


class FileStorage:
    """represent a new class FileStorage

    Attributes:
       __file_path(str): the name of the file where to save objects.
       __objects(dict): a dictionary that store all objects
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary"""
        return FileStorage.__objects
   
    def new(self, obj):
        """set the value of objects"""
        clname = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(clname, obj.id)] = obj

    def save(self):
        """serialize a python object to json string"""
        fobj = FileStorage.__objects
        obj_to_dict = {obj: fobj[obj].to_dict() for obj in fobj.keys()}
        with open(FileStorage.__file_path, "w") as jsonfile:
            json.dump(obj_to_dict, jsonfile)

    def reload(self):
        """deserializes the json file to python objects"""
        try:
            with open(FileStorage.__file_path) as jsonfile:
                json_to_dict = json.load(jsonfile)
                for d in json_to_dict.values():
                    clname = d["__class__"]
                    del d["__class__"]
                    self.new(eval(clname)(**d))
        except FileNotFoundError:
            return
