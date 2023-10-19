#!/usr/bin/python3
"""BaseModel class for AirBnB
"""


from datetime import datetime
import uuid
import models

class BaseModel:
    """Defines the BaseModel"""

    def __init__(self, *args, **kwargs) -> None:
        """initializes the BaseModel and sets the id, created_at, and updated_at properties"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for key in kwargs:
                if key == "updated_at" or key == "created_at":
                    kwargs[key] = datetime.strptime(kwargs[key], time_format)
                if key != "__class__":
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self) -> str:
        """returns the string format "[<class name>] (<self.id>) <self.__dict__>" """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """updates the public instance attribute updated_at with the current data"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self) -> dict:
        """returns a dictionary containing all keys/values of __dict__ of the instance"""
        out = self.__dict__.copy()
        if "created_at" in out:
            out["created_at"] = out["created_at"].isoformat()
        if "updated_at" in out:
            out["updated_at"] = out["updated_at"].isoformat()
        out["__class__"] = self.__class__.__name__
        return out
