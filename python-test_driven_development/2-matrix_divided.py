#!/usr/bin/python3
"""define function that devides all elements of a matrix"""


def matrix_divided(matrix, div):
    """devides all elements of a matrix

    Args:
        matrix (ist): list of lists of integers or floats
        div (int, float): number that can't be equal to 0

    Error:
        TypeError: if matrix isn't a list of integers or float
        TypeError: if row of the matrix aren't of the same size
        TypeError: if div aren't integer or float
        ZeroDivisionError: if div equal to 0

    Return:
        New matrix
    """
    error_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if (
        not isinstance(matrix, list) or matrix == []
        or not all(isinstance(row, list) for row in matrix) or
        not all(isinstance(num, (int, float)) for row in matrix for num in row)
    ):
        raise TypeError(error_msg)
    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
