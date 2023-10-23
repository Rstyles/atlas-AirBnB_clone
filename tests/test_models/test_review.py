import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.review_data = {
            "place_id": "123",
            "user_id": "456",
            "text": "A great place to stay!",
        }

    def test_review_creation(self):
        review = Review(**self.review_data)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, self.review_data["place_id"])
        self.assertEqual(review.user_id, self.review_data["user_id"])
        self.assertEqual(review.text, self.review_data["text"])

    def test_default_values(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        review = Review(**self.review_data)
        review_dict = review.to_dict()
        self.assertIsInstance(review_dict, dict)
        self.assertEqual(review_dict["place_id"], self.review_data["place_id"])
        self.assertEqual(review_dict["user_id"], self.review_data["user_id"])
        self.assertEqual(review_dict["text"], self.review_data["text"])


if __name__ == "__main__":
    unittest.main()
