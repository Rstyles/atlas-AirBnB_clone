import unittest
from models.state import State


class TestState(unittest.TestCase):
    def setUp(self):
        self.state_data = {
            "name": "California",
        }

    def test_state_creation(self):
        state = State(**self.state_data)
        self.assertIsInstance(state, State)
        self.assertEqual(state.name, self.state_data["name"])

    def test_default_values(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_to_dict(self):
        state = State(**self.state_data)
        state_dict = state.to_dict()
        self.assertIsInstance(state_dict, dict)
        self.assertEqual(state_dict["name"], self.state_data["name"])


if __name__ == "__main__":
    unittest.main()
