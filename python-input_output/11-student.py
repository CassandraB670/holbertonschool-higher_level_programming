#!/usr/bin/python3
"""write a class that defines a student"""


class Student:
    """class that defines a student"""

    def __init__(self, first_name, last_name, age):
        """Student

        Args:
            first_name : student's first name
            last_name : student's last name
            age : age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves a dictionary representation

        Return: attributes name"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}

    def reload_from_json(self, json):
        """_summary_

        Args:
            json (_type_): _description_
        """
        for key, value in json.items():
            setattr(self, key, value)
