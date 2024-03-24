#!/usr/bin/python3
""" Import BaseModel class """
from models.base_model import BaseModel


class User(BaseModel):
    """A class for User personal informations"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
