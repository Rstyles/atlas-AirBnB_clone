import unittest
from models.user import User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user_data = {
            "email": "test@example.com",
            "password": "password123",
            "first_name": "John",
            "last_name": "Doe",
        }

    def test_user_creation(self):
        user = User(**self.user_data)
        self.assertIsInstance(user, User)
        self.assertEqual(user.email, self.user_data["email"])
        self.assertEqual(user.password, self.user_data["password"])
        self.assertEqual(user.first_name, self.user_data["first_name"])
        self.assertEqual(user.last_name, self.user_data["last_name"])

    def test_default_values(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_to_dict(self):
        user = User(**self.user_data)
        user_dict = user.to_dict()
        self.assertIsInstance(user_dict, dict)
        self.assertEqual(user_dict["email"], self.user_data["email"])
        self.assertEqual(user_dict["password"], self.user_data["password"])
        self.assertEqual(user_dict["first_name"], self.user_data["first_name"])
        self.assertEqual(user_dict["last_name"], self.user_data["last_name"])

if __name__ == '__main__':
    unittest.main()
