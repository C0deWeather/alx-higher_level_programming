#!/usr/bin/python3


"""This module appends text to the end of a text file"""


def append_write(filename="", text=""):
    """Appends text to the end of a file"""
    with open(filename, 'a') as f:
        n = f.write(text)
    return n
