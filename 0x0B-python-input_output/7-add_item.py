#!/usr/bin/python3


"""This module adds all arguments to a Python list"""


import sys
from os.path import exists


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = 'add_item.json'
if exists(filename):
    arg_list = load_from_json_file(filename)
else:
    arg_list = []

arg_list.extend(sys.argv[1:])
save_to_json_file(arg_list, filename)
