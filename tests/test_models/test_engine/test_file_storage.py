#!/usr/bin/python3
"""Import unittest & file_storage to create unittest & FileStorage classes."""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """A unittest class for FileStorage class."""

    def setUp(self):
        """Method to create instance of BaseModel &
        FileStorage before each test."""
        self.storage = FileStorage()
        self.base_model = BaseModel()
        self.storage.__file_path = "file.json"

    def tearDown(self):
        """Method to remove json file after each test."""
        os.remove(self.obj.__file_path)

    def test_save(self):
        """Method to test serialization objects to json file."""
        self.storage.save()
        with open(self.storage.__file_path) as file:
            data = json.load(file)
            self.assertEqual(data, {"obj": self.storage.__objects
                                    ["obj"].to_dict()})

    def test_all(self):
        """Method to test the return of the dictionary of instances."""
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        """Method to test the set of new object with certain key."""
        self.storage.new(self.base_model)
        obj = self.storage.all()
        self.assertTrue(
            self.base_model.__class__.__name__ + "." +
            self.base_model.id in obj)

    def test_reload(self):
        """Method to test the deserialization of the JSON file to __objects."""
        self.storage.new(self.base_model)
        self.storage.save()
        new_storage = FileStorage()
        new_storage.reload()
        obj = new_storage.all()
        self.assertTrue(
            self.base_model.__class__.__name__ + "." +
            self.base_model.id in obj)


if __name__ == "__main__":
    unittest.main()
