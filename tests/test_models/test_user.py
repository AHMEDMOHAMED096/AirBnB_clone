#!/usr/bin/python3
"""Import unittest & user to create unittest & User classes."""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """A unittest class for User class."""
    def test_user(self):
        """Method to test the initialization of user attributes."""
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")


if __name__ == "__main__":
    unittest.main()
