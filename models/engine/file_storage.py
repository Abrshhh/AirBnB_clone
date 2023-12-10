#!/usr/bin/python3
'''Define a FileStorage class.'''
import json
from models.base_model import BaseModel


class FileStorage:
    '''Represents a FileStorage class that  serializes instances
    to a JSON file and deserializes JSON file to instances.'''

    def __init__(self):
        '''Initialize the class FileStorage.'''
        self.__file_path = "file.json"
        self.__objects = {}

    def all(self):
        ''' '''
        return self.__objects

    def new(self, obj):
        ''' '''
        key = f"{obj.__class__.__name__}{obj.id}"
        self.__objects[key] = obj

    def save(self):
        '''Serializes __objects to the JSON file .'''
        new_dict = {}

        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as f:
            json.dump(new_dict, f)
