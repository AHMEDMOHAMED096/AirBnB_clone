#!/usr/bin/python3
"""Import unittest & user to create unittest & City classes."""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """A unittest class for City class."""
    def test_city(self):
        """Method to test the initialization of city attributes."""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")


if __name__ == "__main__":
    unittest.main()
