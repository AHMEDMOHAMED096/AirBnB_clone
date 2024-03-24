#!/usr/bin/python3
""" Import BaseModel class """
from models.base_model import BaseModel


class City(BaseModel):
    """A class for City objects"""

    state_id = ""
    name = ""
