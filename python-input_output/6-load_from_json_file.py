#!/usr/bin/python3
"""Write a function that creates an Object from a JSON file"""
import json


def load_from_json_file(filename):
    """fct that creates an Object from a JSON file

    Args:
        filename (_type_): _description_
    """
    with open(filename, "r") as f:
        return json.load(f)
