#!/usr/bin/python3
""" Import datetime && uuid && models """
from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """This Class defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        """The constructor for the BaseModel class.

        Parameters:
            args: Positional arguments
            kwargs: Key-word arguments
        """

        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

        else:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue

                elif key == "created_at" or key == "updated_at":
                    date_object = datetime.strptime
                    (value, "%Y-%m-%dT%H:%M:%S.%f")

                    setattr(self, key, date_object)
                else:
                    setattr(self, key, value)

    def __str__(self):
        """
        This method returns nicely readable string representation of an object.
        """
        return "[{}] ({}) {}".format
        (self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        updates the public instance attribute updated_at
        with the current datetime.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """This method returns the dictionary representation of an instance."""
        dict = {
            "id": self.id,
            "__class__": self.__class__.__name__,
        }
        if hasattr(self, "created_at"):
            dict["created_at"] = self.created_at.isoformat()
        if hasattr(self, "updated_at"):
            dict["updated_at"] = self.updated_at.isoformat()
        return dict
