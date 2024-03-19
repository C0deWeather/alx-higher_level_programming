#!/usr/bin/python3
def max_integer(my_list=[]):
    """
    Finds the biggest integer in a list.

    Args:
    my_list (list): int list

    Returns:
    int: the biggest integer in the list
    """
    if my_list == []:
        return None
    i = 0
    i_max = my_list[i]
    while i < len(my_list) - 1:
        if my_list[i + 1] > i_max:
            i_max = my_list[i + 1]
        i += 1
    return i_max
