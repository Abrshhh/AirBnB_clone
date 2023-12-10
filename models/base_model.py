#!/usr/bin/python3
from datetime import datetime
import uuid
'''Define a class BaseModel.'''


class BaseModel:
    '''Represents the class BaseModel.'''

    def __init__(self, *args, **kwargs):
        '''Initializes the class BaseModel.'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if kwargs:
            self.id = kwargs.get("id", self.id)
            self.created_at = kwargs.get("created_at", self.created_at)
            self.updated_at = kwargs.get("updated_at", self.updated_at)

        if isinstance(self.created_at, str):
            self.created_at = datetime.strptime(self.created_at.isoformat())
        if isinstance(self.updated_at, str):
            self.updated_at = datetime.strptime(self.updated_at.isoformat())

    def __str__(self):
        print(f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        '''Updates updated_at with the current datetime.'''

        self.updated_at = datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values
        of __dict__ of the instance.'''

        return {"id": self.id,
                "__class__": self.__class__.__name__,
                "self.created_at": self.created_at.isoformat(),
                "self.updated_at": self.updated_at.isoformat()
                }
