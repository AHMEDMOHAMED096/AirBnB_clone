#!/usr/bin/python3
"""Import unittest & state to create unittest & State classes."""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """A unittest class for State class."""
    def test_state(self):
        """Method to test the initialization of state attributes."""
        state = State()
        self.assertEqual(state.name, "")


if __name__ == "__main__":
    unittest.main()
