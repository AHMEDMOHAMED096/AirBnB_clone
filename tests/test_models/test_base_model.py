#!/usr/bin/python3
"""Import unittest & base_model to create unittest & BaseModel classes."""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """A unittest class for BaseModel class."""

    def setUp(self):
        """Method to create instance of BaseModel before every test."""
        self.base_model = BaseModel()

    def test_attributes(self):
        """Method to test the initialization of instance attributes."""
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_id_generation(self):
        """Method to test existence of id and check its type"""
        self.assertIsNotNone(self.base_model.id)
        self.assertIsInstance(self.base_model.id, str)

    def test_created_at(self):
        """Method to test the relation of an instance"""
        self.assertIsInstance(self.base_model.created_at, datetime)

    def test_updated_at(self):
        """Method to test the relation of an instance"""
        self.assertIsInstance(self.base_model.updated_at, datetime)

    def test_to_dict_method(self):
        """Method to test functionality of 'to_dict' method"""
        keys = ["id", "created_at", "updated_at", "__class__"]
        model_dict = self.base_model.to_dict()
        self.assertCountEqual(model_dict.keys(), keys)
        self.assertEqual(model_dict["__class__"], "BaseModel")

    def test_str_method(self):
        """Method to test functionality of '__str__' method"""
        output = f"[BaseModel]({self.base_model.id})
        {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), output)


if __name__ == "__main__":
    unittest.main()
