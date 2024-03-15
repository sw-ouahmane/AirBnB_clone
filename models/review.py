#!/usr/bin/python3
""" Module that contains class Review """
from models.base_model import BaseModel


class Review(BaseModel):
    """Review class"""
    place_id: str = ""
    user_id: str = ""
    text: str = ""
