#!/usr/bin/python3
"""module class of review"""
from models.base_model import BaseModel

class Review(BaseModel):
    """class review which inherits BaseModel"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)