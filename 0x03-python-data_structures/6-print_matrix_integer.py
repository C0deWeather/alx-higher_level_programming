#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    """
    Prints a matrix of integers

    Args:
    matrix: the matrix
    """
    for row in matrix:
        for i in range(len(row)):
            if i == len(row) - 1:
                # If it's the last element of the row, print without a space
                print("{:d}".format(row[i]), end="")
            else:
                # Otherwise, print with a space
                print("{:d}".format(row[i]), end=" ")
        print()  # Move to the next line after printing each row
