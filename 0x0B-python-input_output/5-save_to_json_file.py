#!/usr/bin/python3


"""Writes an Object to a text file, using a JSON representation"""


import json


def save_to_json_file(my_obj, filename):
    """
    Writes an object to a text file, using a JSON representation

    Args:
    my_obj (obj): the object
    filename (str): file name
    """
    j_str = json.dumps(my_obj)
    with open(filename, 'w') as f:
        f.write(j_str) 
