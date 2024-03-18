#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list is not None:
        i = len(my_list) - 1
    while my_list is not None and i >= 0:
        print("{:d}".format(my_list[i]))
        i -= 1
