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
