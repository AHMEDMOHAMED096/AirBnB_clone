#!/usr/bin/python3
""" Import json module. """

import json


class FileStorage:
    """A class that serializes instances to a JSON file
    and deserializes JSON file to instances."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """This method returns the dictionary of instances."""
        return self.__objects.copy()

    def new(self, obj):
        """This method sets in __objects the obj with
        key <obj class name>.id."""
        self.__objects[obj.__class__.__name__ + "." + obj.id] = obj

    def save(self):
        """This method serializes __objects to the JSON file."""

        with open(self.__file_path, "w") as file:
            if not self.__objects:
                file.write("")

            else:
                json_data = {}
                for key, value in self.__objects.items():
                    json_data[key] = value.to_dict()
                file.write(json.dumps(json_data, indent=4))

    def reload(self):
        """This method deserializes the JSON file to __objects."""

        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.city import City
        from models.place import Place
        from models.state import State
        from models.review import Review

        classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review,
        }
        try:
            with open(self.__file_path) as file:
                data = json.load(file)

            for key, value in data.items():
                class_name = key.split(".")[0]
                if class_name in classes:
                    self.__objects[key] = classes[class_name](**value)

        except FileNotFoundError:
            pass
