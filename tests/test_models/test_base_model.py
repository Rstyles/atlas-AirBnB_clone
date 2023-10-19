#!/usr/bin/python3
"""Unit Tests for models/base_model.py"""
import os
import unittest
import uuid
from datetime import datetime
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    def test_init_without_args(self):
        obj = BaseModel()
        self.assertTrue(hasattr(obj, "id"))
        self.assertTrue(hasattr(obj, "created_at"))
        self.assertTrue(hasattr(obj, "updated_at"))
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)

    def test_init_with_kwargs(self):
        data = {
            "id": "test_id",
            "created_at": "2023-10-18T12:00:00.000000",
            "updated_at": "2023-10-18T12:01:00.000000",
            "custom_field": "test_value",
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, data["id"])
        self.assertEqual(obj.created_at, datetime.fromisoformat(data["created_at"]))
        self.assertEqual(obj.updated_at, datetime.fromisoformat(data["updated_at"]))
        self.assertEqual(obj.custom_field, "test_value")

    def test_str_method(self):
        obj = BaseModel()
        expected_str = f"[BaseModel] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_str)

    def test_save_method(self):
        obj = BaseModel()
        original_updated_at = obj.updated_at
        obj.save()
        self.assertNotEqual(original_updated_at, obj.updated_at)

    def test_to_dict_method(self):
        obj = BaseModel()
        obj_dict = obj.to_dict()
        self.assertTrue(isinstance(obj_dict, dict))
        self.assertIn("__class__", obj_dict)
        self.assertIn("id", obj_dict)
        self.assertIn("created_at", obj_dict)
        self.assertIn("updated_at", obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(obj_dict["id"], obj.id)
        self.assertEqual(obj_dict["created_at"], obj.created_at.isoformat())
        self.assertEqual(obj_dict["updated_at"], obj.updated_at.isoformat())


if __name__ == "__main__":
    unittest.main()
