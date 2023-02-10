#!/usr/bin/python3
""" model of Amenity class"""

from models.base_model import BaseModel

class Amenity(BaseModel):
    """class amenity inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)