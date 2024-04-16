#!/usr/bin/python3


"""This module reads a text file"""


def read_file(filename=""):
    """Reads a text file and prints to stdout"""
    with open(filename, 'r') as file:
        content = file.read()
        print(content)
