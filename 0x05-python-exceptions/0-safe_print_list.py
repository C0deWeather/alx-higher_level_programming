#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        for e in my_list:
            if i == x:
                break
            print(e, end="")
            i += 1
        print()
        return i
    except IndexError:
        print()
        return i
