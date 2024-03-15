#!/usr/bin/python3
"""
    instantiates the storage system, and defines
    classes for further use
"""
import models
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

from models.engine.file_storage import FileStorage

classes_dict = {
    "BaseModel": BaseModel,
    "User": User,
    "Place": Place,
    "State": State,
    "City": City,
    "Amenity": Amenity,
    "Review": Review,
}
storage: FileStorage = FileStorage()
storage.reload()
