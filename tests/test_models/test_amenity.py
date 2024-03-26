#!/usr/bin/python3
"""Import unittest & user to create unittest & Amenity classes."""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """A unittest class for Amenity class."""
    def test_amenity(self):
        """Method to test the initialization of amenity attributes."""
        amenity = Amenity()
        self.assertEqual(amenity.name, "")


if __name__ == "__main__":
    unittest.main()
