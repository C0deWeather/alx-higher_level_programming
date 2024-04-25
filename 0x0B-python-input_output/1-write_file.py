#!/usr/bin/python3


"""This module writes a string to a file"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    n = 0
    with open(filename, 'w') as f:
        n = f.write(text)
    return n
