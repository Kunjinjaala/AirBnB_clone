#!/usr/bin/python3
"""A User class model"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing place objects"""

    state_id = ""
    name = ""
