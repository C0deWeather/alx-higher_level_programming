#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Deletes the item at a specific position in a list

    Args:
    my_list (list): the list
    idx (int): the index

    Returns:
    list: returns the modified list
    """

    if my_list == [] or idx >= len(my_list) or idx < 0:
        return my_list

    del my_list[idx]
    return my_list
