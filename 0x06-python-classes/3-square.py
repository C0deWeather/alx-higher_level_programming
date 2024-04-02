#!/usr/bin/python3

"""
This module defines a class to represent a square object.
"""


class Square:
    """
    Defines a square
    """
    def __init__(self, size=0):
        """
        Creates a square of size <__size>

        Args:
        size (int): size of square
        """
        self.__size = size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """
        Returs the current square area
        """
        return sel.__size ** 2
