#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Calculates the weighted average of all integers tuple

    Arguments:
    my_list (list): the list containing tuples

    Returns:
    float: Calculated average
    """
    p_sum = 0
    w_sum = 0
    if my_list == []:
        return 0
    for s, w in my_list:
        p_sum += s * w
        w_sum += w
    return p_sum / w_sum
