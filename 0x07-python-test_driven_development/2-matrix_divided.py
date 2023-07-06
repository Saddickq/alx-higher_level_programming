#!/usr/bin/python3
"""
A module that divides a matrix
"""


def matrix_divided(matrix, div):
    """A function that divide a matrix with the number div"""

    outer_list = []
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    size = len(matrix[0])

    for row in matrix:
        inner_list = []
        if type(row) is not list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        if (size != len(row)):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if type(num) is not int and type(num) is not float:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            inner_list.append(round(num / div, 2))
        outer_list.append(inner_list)
    return (outer_list)
