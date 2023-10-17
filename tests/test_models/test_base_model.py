#!/usr/bin/python3
from models.base_model import BaseModel

import unittest
import models.base_model

class TestBase_model(unittest.TestCase):
    def test_new(self):
        my_model = BaseModel()
        my_model.name = "My First Model"
        my_model.my_number = 89
        self.assertTrue(my_model.name == 'My First Model')
        self.assertTrue(my_model.my_number == 89)