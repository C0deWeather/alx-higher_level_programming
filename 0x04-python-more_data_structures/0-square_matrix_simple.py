#!/usr/bin/python3
def pow(a):
    return (a ** 2)


def square_matrix_simple(matrix=[]):
    """
    Squares the elements of a matrix

    Argument:
    matrix (matrix): The input matrix.

    Returns:
    matrix: A modified independent copy of the initial matrix
    """
    new_matrix = []

    try:
        for row in matrix:
            new_row = list(map(pow, row))
            new_matrix.append(new_row)
        return new_matrix

    except TypeError:
        return None
