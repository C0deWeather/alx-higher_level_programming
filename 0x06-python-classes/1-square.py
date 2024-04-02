#!/usr/bin/python3

"""
This module defines a class to represent a square object.
"""


class Square:
    """
    Defines a square
    """
    def __init__(self, size):
        """
        Creates a square of size <__size>

        Args:
        size (int): size of square
        """
        self.__size = size
