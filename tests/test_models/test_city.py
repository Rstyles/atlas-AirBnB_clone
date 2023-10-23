import unittest
from models.city import City


class TestCity(unittest.TestCase):
    def setUp(self):
        self.city_data = {
            "state_id": "123",
            "name": "San Francisco",
        }

    def test_city_creation(self):
        city = City(**self.city_data)
        self.assertIsInstance(city, City)
        self.assertEqual(city.state_id, self.city_data["state_id"])
        self.assertEqual(city.name, self.city_data["name"])

    def test_default_values(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        city = City(**self.city_data)
        city_dict = city.to_dict()
        self.assertIsInstance(city_dict, dict)
        self.assertEqual(city_dict["state_id"], self.city_data["state_id"])
        self.assertEqual(city_dict["name"], self.city_data["name"])


if __name__ == "__main__":
    unittest.main()
