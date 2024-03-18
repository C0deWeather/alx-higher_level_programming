#!/usr/bin/python3

def no_c(my_string):
    """
    Removes all characters c and C from a string.

    Args:
    my_string (str): Original string

    Returns:
    str: a new string without the removed chars
    """
    i = 0
    mod_list = list(my_string)
    for char in mod_list:
        if char in "cC":
            del mod_list[i]
        i += 1
    return "".join(mod_list)
