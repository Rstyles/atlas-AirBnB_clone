#!/usr/bin/python3
""" City model
"""
from models.base_model import BaseModel


class City(BaseModel):
    state_id: str = ""
    name: str = ""
