#!/usr/bin/python3
"""2-matrix_divided

This module includes a function matrix_divided
"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div

    All elements of matrix must be int or float
    div must be an integer or float different than zero

    Returns a new matrix
    """
    def isListOfListsOfNumbers(matrix):
        if (type(matrix) is not list):
            return False
        if (len(matrix) == 0):
            return True
        for row in matrix:
            if (type(row) is not list):
                return False
            if (not all(map(lambda x: type(x) in [int, float], row))):
                return False
        return True
    if (not isListOfListsOfNumbers(matrix)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if (len({len(row) for row in matrix}) > 1):
        raise TypeError("Each row of the matrix must have the same size")
    if (type(div) not in [float, int]):
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")
    return [list(map(lambda x: round(x / div, 2), row)) for row in matrix]
