#!/usr/bin/python3


"""This module converts a string to its object representation"""


import json


def from_json_string(my_str):
    """converts a json string to its object"""
    return json.loads(my_str)
