#!/usr/bin/python3

def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Arguments:
    a_dictionary (dict): the dictionary

    Returns:
    string: returns the key with the biggest integer value
    """
    try:
        if a_dictionary is None:
            return None
        v_max = max(a_dictionary.values())
        for key, value in a_dictionary.items():
            if value == v_max:
                return key
    except ValueError:
        return None
