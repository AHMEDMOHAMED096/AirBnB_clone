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

        if kwargs:
            for key in kwargs:
                if key != "__class__":
                    setattr(self, key, kwargs[key])

            if "created_at" in kwargs:
                self.created_at = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")

            if "updated_at" in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

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
        dict = self.__dict__.copy()
        dict["__class__"] = self.__class__.__name__
        dict["created_at"] = dict["created_at"].isoformat()
        dict["updated_at"] = dict["updated_at"].isoformat()
        return dict
