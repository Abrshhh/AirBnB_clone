#!/usr/bin/python3

import cmd
import json
from base_model import BaseModel


class HBNBCommand(cmd.Cmd):

    prompt = "(hbnb)"

    def do_create(self, instance):
        """This command creates a new instance to BaseModel\
            saves it to json file and prints its id."""

        instance = BaseModel()
        dict_instance = instance.__dict__

        with open("file.json", 'w') as f:
            json.dump(dict_instance, f)

        print(dict_instance.id)

    def do_quit(self, arg):
        '''This command quits the program.'''
        return True

    do_EOF = do_quit


if __name__ == '__main__':
    HBNBCommand().cmdloop()
