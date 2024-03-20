#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list (once for each integer)

    Arguments:
    my_list (list): The initial list

    Returns:
    int: The sum
    """
    n_sum = 0
    try:
        my_set = set(my_list)
        for element in my_set:
            n_sum += element
        return n_sum
    except TypeError:
        return None
