#!/usr/bin/python3
""" module class of state"""
from models.base_model import BaseModel

class State(BaseModel):
    """class state which inherits from BaseModel"""
    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__int__(*args, **kwargs)