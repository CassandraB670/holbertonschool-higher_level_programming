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

    @staticmethod
    def from_json_string(json_string):
        """return the list of the JSON string representation

        Args:
            json_string : string representing a list of dictionaries
        """
        if json_string is None or json_string == []:
            return []
        return json.loads(json_string)

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

    @classmethod
    def create(cls, **dictionary):
        """return an instance with all attributes already set

        Args:
            cls (class): The class of the instance to be created.
            dictionary (dict): A dictionary of attributes for the new instance.
        Returns:
            object: Instance of the class with attributes from the dict.
        """
        if cls.__name__ == "Rectangle":
            new = cls(10, 10)
        else:
            new = cls(10)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """_summary_
        """
        filename = f"{cls.__name__}.json"
        instance_list = []

        try:
            with open(filename, 'r') as file:
                json_str = file.read()
                json_data = cls.from_json_string(json_str)

                for data in json_data:
                    instance = cls.create(**data)
                    instance_list.append(instance)

        except FileNotFoundError:
            pass

        return instance_list
