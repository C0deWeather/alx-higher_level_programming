#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.

    Args:
    my_list (list): int list

    Returns:
    int: the biggest integer in the list
    """
    i_max = 0
    if my_list == []:
        return None
    for i in my_list:
        if i > i_max:
            i_max = i
    return i_max
