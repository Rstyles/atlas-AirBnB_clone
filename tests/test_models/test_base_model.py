#!/usr/bin/python3
"""Unit tests for BaseModel"""


from models.base_model import BaseModel
import unittest


class Test_Base_model(unittest.TestCase):
    def test_new(self):
        """assert new item created with set values"""
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertTrue(my_model.name == "My First Model")
        self.assertTrue(my_model.my_number == 89)

    def test_save(self):
        model = BaseModel()
        time_before_save = model.updated_at
        model.save()
        time_after_save = model.updated_at
        self.assertTrue(time_before_save != time_after_save)
        
    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        
    def test_str__(self):
        model = BaseModel()
        compare_str = f"[{model.__class__.__name__}] ({model.id}) {model.__dict__}"
        output_str = model.__str__()
        self.assertTrue(output_str != None)
