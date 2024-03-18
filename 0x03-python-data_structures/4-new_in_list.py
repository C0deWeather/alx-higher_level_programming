#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replaces an element at idx in a list.

    Args:
    my_list (list): the list
    idx (int): index of element in list
    element: the replacement

    Returns:
    list: a new list containing the replacement
    """

    new_list = my_list.copy()

    if idx >= len(my_list) or idx < 0:
        return new_list

    new_list[idx] = element
    return new_list
