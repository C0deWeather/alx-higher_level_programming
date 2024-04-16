#!/usr/bin/python3


"""This module converts data to json format"""


import json

def to_json_string(my_obj):
    """converts object to json format"""
    return json.dumps(my_obj)
