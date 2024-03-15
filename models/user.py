#!/usr/bin/python3
""" Module that contains class User """
from models.base_model import BaseModel


class User(BaseModel):
    """User class"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
