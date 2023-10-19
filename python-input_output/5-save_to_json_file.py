#!/usr/bin/python3
"""Write a function that writes an Object to a text file,
using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """fct that writes an Object to a text file, usin JSON

    Args:
        my_obj (): obj
        filename (): name of the file
    """
    with open(filename, "w") as f:
        json_object = json.dumps(my_obj)
        f.write(json_object)
        f.close()
