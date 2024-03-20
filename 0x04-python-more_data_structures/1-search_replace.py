#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replaces all occurences of an element by another in al new list.

    Arguments:
    my_list (list): The initial list.
    search: the element to replace in the list.
    replace: The new element.

    Returns:
    list: The new list
    """
    try:
        new_list = []
        for element in my_list:
            if element == search:
                new_list.append(replace)
            else:
                new_list.append(element)
        return new_list

    except TypeError:
        return my_list
