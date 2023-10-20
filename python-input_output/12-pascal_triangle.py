#!/usr/bin/python3
"""Create a function that returns a list of lists of integers
representing the Pascal's triangle of n"""


def pascal_triangle(n):
    """fct that returns a list of lists of integers

    Args:
        n (_type_): _description_

    Return : list of lists of integers
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for index1 in range(1, n):
        prev_row = triangle[-1]
        new_row = [1]

        for index2 in range(1, index1):
            new_value = prev_row[index2 - 1] + prev_row[index2]
            new_row.append(new_value)

        new_row.append(1)
        triangle.append(new_row)

    return triangle
