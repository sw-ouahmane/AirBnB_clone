#!/usr/bin/python3
""" Module that contains class BaseModel """

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base class"""

    def __init__(self, *args, **my_dict):
        """ constructor for BaseModel class """
        if my_dict:
            for key, value in my_dict.items():
                if key == "created_at" or key == "updated_at":
                    t = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, t)
                elif key == "__class__":
                    continue
                else:
                    setattr(self, key, value)
        else:
            self.id: str = str(uuid4())
            self.created_at: datetime = datetime.now()
            self.updated_at: datetime = self.created_at

    def __str__(self) -> str:
        """ string representation of BaseModel class """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self) -> None:
        """ updates the self.updated_at """
        self.updated_at = datetime.now()
        from models import storage
        storage.new(self)
        storage.save()

    def to_dict(self) -> dict:
        """ returns a dict representation of instance"""
        my_dict = self.__dict__.copy()
        my_dict.update({"__class__": self.__class__.__name__})
        my_dict.update({"created_at": str(self.created_at.isoformat())})
        my_dict.update({"updated_at": str(self.updated_at.isoformat())})
        return my_dict
