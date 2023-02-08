#!/usr/bin/python3
"""module of the cmd interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review  import Review

class_list = { "BaseModel": BaseModel, "User": State}