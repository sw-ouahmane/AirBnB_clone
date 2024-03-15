#!/usr/bin/python3
""" Module that contains class FileStorage """
from json import load, dump


class FileStorage:
    """FileStorage class"""
    __file_path: str = "file.json"
    __objects: dict = {}

    @property
    def file_path(self):
        '''returns self.__file_path'''
        return self.__file_path

    def all(self) -> dict:
        """return data dict"""
        return self.__objects

    def reload(self) -> None:
        """reload method to read from file.json and update self.__objects"""
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                loaded_dict = load(f)
            from models import classes_dict
            for key, my_dict in loaded_dict.items():
                class_name, _ = key.split('.')
                obj = classes_dict[class_name](**my_dict)
                self.__objects.update({key: obj})
        except FileNotFoundError:
            pass

    def save(self) -> None:
        """saves self.__objects to file.json"""
        saved_dict = {key: obj.to_dict()
                      for key, obj in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            dump(saved_dict, f)

    def new(self, obj) -> None:
        """new element is added to self.__objects"""
        key: str = obj.__class__.__name__ + "." + obj.id
        self.__objects.update({key: obj})
