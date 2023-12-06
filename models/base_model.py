#!/usr/bin/python3
import datetime

'''Define a class BaseModel.'''


class BaseModel:
    '''Represents the class BaseModel.'''

    def __init__(self, *args, **kwargs):
        '''Initializes the class BaseModel.'''

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

        if len(kwargs) != 0:


    def __str__(self):
        print(f"[BaseModel] ({self.id}) {self.__dict__}")

    def save(self):
        '''Updates updated_at with the current datetime.'''

        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        '''Returns a dictionary containing all keys/values
        of __dict__ of the instance.'''

        self.created_at = self.created_at.isoformat()
        self.updated_at = self.updated_at.isoformat()
        self.__dict__ = dict(id=str(uuid.uuid4())
                             created_at=self.created_at.isoformat()
                             updated_at=self.updated_at.isoformat()
                             )
