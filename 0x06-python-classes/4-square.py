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

    @attribute.setter
    def size(self, value):
        """
        sets the value of size
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        return self.__size

    @property
    def size(self):
        """
        Retrieves the value of size
        """
        return self.__size

    def area(sef):
        """
        Returs the current square area
        """
        return self.__size ** 2
