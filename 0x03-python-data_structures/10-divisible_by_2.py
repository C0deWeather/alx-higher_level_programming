#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Finds all multiples of 2 in a list

    Args:
    my_list (list): the list

    Returns:
    list: Return a new list with True or False, depending on whether
     the integer at the same position in the original list is a multiple of 2
    """
    list_result = []
    for i in my_list:
        if i % 2 == 0:
            list_result.append(True)
        else:
            list_result.append(False)
    return list_result
