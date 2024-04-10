#!/usr/bin/python3

"""This module handles division on matrices"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix"""

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")

    m = []
    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
        n_row = []
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(
                    "matrix must be a matrix (list of lists) \
of integers/floats")
            n_row.append(round(i / div, 2))
        m.append(n_row)
    return m
