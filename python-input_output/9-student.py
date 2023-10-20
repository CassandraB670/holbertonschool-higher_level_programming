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

    def to_json(self):
        """retrieves a dictionary representation"""
        return self.__dict__
