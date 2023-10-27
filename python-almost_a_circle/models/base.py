#!/usr/bin/python3
"""Write the first class Base"""

import json


class Base:
    """base of all other classes in this project"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialisation

        Args:
            id : id of the object. Defaults to None.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries

        Args:
            list_dictionaries : list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == "[]":
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """write the JSON string representation of list_objs to a file

        Args:
            list_objs : list of instances who inherits of Base
        """
        if list_objs is None:
            list_objs = []

        filename = f"{cls.__name__}.json"
        data = [obj.to_dictionary() for obj in list_objs]
        json_str = Base.to_json_string(data)

        with open(filename, 'w') as file:
            file.write(json_str)
