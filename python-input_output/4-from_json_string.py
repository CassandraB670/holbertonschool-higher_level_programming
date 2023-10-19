#!/usr/bin/python3
"""Write a function that returns an object represented by a JSON string"""
import json


def from_json_string(my_str):
    """fct that returns an object represented by a JSON string

    Args:
        my_str (_type_): _description_

    Return: object represented by a JSON string
    """
    return json.loads(my_str)
