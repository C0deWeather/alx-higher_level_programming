#!/usr/bin/python3


"""This module deserializes a JSON file"""


import json


def load_from_json_file(filename):
    """Deserializes  a JSON file"""
    with open(filename, 'r') as f:
        return json.load(f)
