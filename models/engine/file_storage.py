#!/usr/bin/python3
"""module of 'FileStorage' class"""

import os.path
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class_list = { "BaseModel": BaseModel, "User": User, "State": State, "City": City, "Amenity": Amenity, "Place": Place, "Review": Review }
white_list = []
for key in class_list:
    white_list.append(key)

class FileStorage():
    """Representation of a FileStorage"""
    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """class constructor"""
        pass

    def all(self):
         """return the dictionary '__objects'"""
         return self.__objects
    
    def new(self, obj):
        """sets in '__objects' the 'obj' with key '<obj class name>.id'"""
        key = obj.__class__.__name__+"."+obj.id
        self.__objects.update({key:obj})

    def save(self):
        """serializes '__objects' to the Json file (__file_path)"""
        dict = {}
        for key in self.__objects:
            dict[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(dict, f)

    def reload(self):
        """deserializes the Json file to '__objects' (only if the Json file exists, otherwise do nothing. if the file !== exists, no exception should be raised)"""
        try:
            with open(self.__file_path, 'r') as f:
                dict = json.load(f)
            for i in dict:
                self.__objects[i] = class_list[dict[i]["__class__"]](**dict[i])
        expect:
            pass
    