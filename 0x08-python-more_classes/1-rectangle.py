#!/usr/bin/python3


"""This module defines a rectangle"""


class Rectangle:
    """This class represents a rectangle"""

    def __init__(self, width=0, height=0):
        """Creates an instance of the class"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Retrieves the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieves the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the value of height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
