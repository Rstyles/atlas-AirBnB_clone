import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity_data = {
            "name": "Wi-Fi",
        }

    def test_amenity_creation(self):
        amenity = Amenity(**self.amenity_data)
        self.assertIsInstance(amenity, Amenity)
        self.assertEqual(amenity.name, self.amenity_data["name"])

    def test_default_values(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_to_dict(self):
        amenity = Amenity(**self.amenity_data)
        amenity_dict = amenity.to_dict()
        self.assertIsInstance(amenity_dict, dict)
        self.assertEqual(amenity_dict["name"], self.amenity_data["name"])


if __name__ == "__main__":
    unittest.main()
