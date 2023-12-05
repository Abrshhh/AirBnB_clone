#!/usr/bin/python3
from datetime import datetime

'''Define a class BaseModel.'''


class BaseModel:
    '''Represents the class BaseModel.'''

    def __init__(self):
        '''Initializes the class BaseModel.'''

        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at =

        def __str__(self):
            print(f"[BaseModel] {self.id} {self.__dict__}")
