import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.place_data = {
            "city_id": "123",
            "user_id": "456",
            "name": "Cozy Cabin",
            "description": "A cozy cabin in the woods.",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 100,
            "latitude": 37.7749,
            "longitude": -122.4194,
            "amenity_ids": [1, 2, 3],
        }

    def test_place_creation(self):
        place = Place(**self.place_data)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, self.place_data["city_id"])
        self.assertEqual(place.user_id, self.place_data["user_id"])
        self.assertEqual(place.name, self.place_data["name"])
        # Add similar assertions for other attributes

    def test_default_values(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        # Add similar assertions for other attributes

    def test_to_dict(self):
        place = Place(**self.place_data)
        place_dict = place.to_dict()
        self.assertIsInstance(place_dict, dict)
        self.assertEqual(place_dict["city_id"], self.place_data["city_id"])
        self.assertEqual(place_dict["user_id"], self.place_data["user_id"])
        self.assertEqual(place_dict["name"], self.place_data["name"])
        # Add similar assertions for other attributes


if __name__ == "__main__":
    unittest.main()
