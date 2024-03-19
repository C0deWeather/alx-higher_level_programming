#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """
    Adds two tuples

    Args:
    tuple_a: the first tuple
    tuple_b: the second tuple

    Returns:
    tuple: returns a tuple with two integers,
     the element-wise sum of the input tuples
    """
    a1 = 0
    a2 = 0
    b1 = 0
    b2 = 0

    # get parameters from tuple_a
    if len(tuple_a) >= 2:
        a1 = tuple_a[0]
        a2 = tuple_a[1]
    elif len(tuple_a) < 2:
        if tuple_a == ():  # empty tuple
            pass
        else:
            a1 = tuple_a[0]  # unity tuple

    # get parameters from tuple_b
    if len(tuple_b) >= 2:
        b1 = tuple_b[0]
        b2 = tuple_b[1]
    elif len(tuple_b) < 2:
        if tuple_b == ():  # empty tuple
            pass
        else:
            b1 = tuple_b[0]  # unity tuple

    return (a1 + b1, a2 + b2)
