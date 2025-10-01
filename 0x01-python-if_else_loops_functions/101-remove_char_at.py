#!/usr/bin/python3

def remove_char_at(str, n):
    """
    Returns a new string with the char at n removed

    Parameters:
        str (string): String to be modified
        n (int): Index of char to be removed

    Returns:
        string: A new string with the char at n removed
    """
    l_str = list(str)
    new_list = []

    for char in l_str:
        if l_str[n] == char:
            continue
        else:
            new_list.append(char)

    return "".join(new_list)
