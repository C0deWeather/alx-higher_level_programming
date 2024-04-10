#!/usr/bin/python3

"""This module adds integers"""

def add_integer(a, b=98):
    """
    Adds two integers

    Args:
    a (int): the first integer
    b (int): the second integer

    Returns:
    int: the sum of the two integers
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) in [float]:
        a = int(a)
    if type(b) in [float]:
        b = int(b)
    return a + b
