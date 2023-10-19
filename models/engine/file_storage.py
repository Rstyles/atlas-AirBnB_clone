#!/usr/bin/python3
"""This module rovides a simple way to serialize and deserialize Python objects to and from a JSON file.
"""
from models.base_model import BaseModel
import json
import os


class FileStorage:
    """
    This class provides a simple way to serialize and deserialize Python objects to and from a JSON file.
    """

    __file_path: str = "file.json"
    __objects: dict = {}

    def all(self) -> dict:
        """
        Retrieve all stored objects from the JSON file.

        Returns:
            dict: A dictionary containing all the stored objects.
        """
        return self.__objects

    def new(self, obj: object) -> None:
        """
        Add a new object to the storage.

        Args:
            obj (object): The object to be added to the storage.

        Returns:
            None
        """
        self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self) -> None:
        """
        Serialize and save the stored objects to the JSON file.

        Returns:
            None
        """
        obj: dict = {}
        for key, value in self.__objects.items():
            obj[key] = value.to_dict()

        with open(self.__file_path, "w") as json_file:
            json.dump(obj, json_file)

    def reload(self) -> None:
        """
        Deserialize and load objects from the JSON file into the storage.

        Returns:
            None
        """
        try:
            if os.path.exists(self.__file_path):
                with open(self.__file_path, "r", encoding="utf-8") as json_file:
                    for key, value in json.load(json_file).items():
                        value = eval(key.split(".")[0])(**value)
                        self.__objects[key] = value
        except FileNotFoundError:
            pass
