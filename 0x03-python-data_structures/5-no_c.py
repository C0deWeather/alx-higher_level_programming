#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all characters c and C from a string.

    Args:
    my_string (str): Original string

    Returns:
    str: a new string without the removed chars
    """
    new_string = ""
    for c in my_string:
        if c not in 'cC':
            new_string += c
    return new_string
