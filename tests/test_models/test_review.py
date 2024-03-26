#!/usr/bin/python3
"""Import unittest & user to create unittest & Review classes."""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """A unittest class for Review class."""
    def test_review(self):
        """Method to test the initialization of review attributes."""
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")


if __name__ == "__main__":
    unittest.main()
