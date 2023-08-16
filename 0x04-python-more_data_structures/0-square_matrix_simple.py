#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers in a matrix.

    Args:
        matrix (list[list]): A 2-dimensional list of integers.

    Returns:
        list[list]: A new matrix where each value is the square of the
                    corresponding value in the input matrix. The initial
                    matrix remains unmodified.
    """
    squared_matrix = [list(map((lambda x: x * x), row)) for row in matrix]
    return squared_matrix
