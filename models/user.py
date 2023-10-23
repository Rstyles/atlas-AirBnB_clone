#!/usr/bin/python3
""" User model
"""
from models.base_model import BaseModel

class User(BaseModel):
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str = ""
        
