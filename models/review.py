#!/usr/bin/python3
""" Import BaseModel class """
from models.base_model import BaseModel


class Review(BaseModel):
    """A class for Reviews"""

    place_id = ""
    user_id = ""
    text = ""
