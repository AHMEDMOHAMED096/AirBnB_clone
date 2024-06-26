#!/usr/bin/python3
"""Import unittest & user to create unittest & Place classes."""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """A unittest class for Place class."""
    def test_place(self):
        """Method to test the initialization of place attributes."""
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, "")
        self.assertEqual(place.number_bathrooms, "")
        self.assertEqual(place.max_guest, "")
        self.assertEqual(place.price_by_night, "")
        self.assertEqual(place.latitude, "")
        self.assertEqual(place.longitude, "")
        self.assertEqual(place.amenity_ids, "")


if __name__ == "__main__":
    unittest.main()
