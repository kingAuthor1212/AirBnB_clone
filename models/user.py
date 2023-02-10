#!/usr/bin/python3
"""module class of User"""

from models.base_model import BaseModel

class User(BaseModel):
    """class User that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __int__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)