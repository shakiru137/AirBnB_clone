#!/usr/bin/python3
"""
a class BaseModel that defines all common attributes/methods for other classes:
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs:
            for k, v in kwargs.items():
                if k == "__class__":
                    continue
                elif k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.strptime(v, time_format))
                else:
                    setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = datetime.utcnow()

        models.storage.new(self)

    def save(self):
        """
        Saves the object to the database.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the object.
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
        
    def __str__(self):
        """
        Returns a string representation of the object.
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)