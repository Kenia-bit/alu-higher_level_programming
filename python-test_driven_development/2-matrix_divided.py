#!/usr/bin/python3
"""
This module defines the matrix_divided function,
which divides all elements of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers/floats.
        div (int or float): The divisor.

    Returns:
        A new matrix with all elements divided by div, rounded to 2 decimal places.

    Raises:
        TypeError: If matrix is not a list of lists of integers/floats.
        TypeError: If rows in the matrix are not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is 0.
    """
    if not isinstance(matrix, list) or any(
        not isinstance(row, list) for row in matrix
    ):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    row_length = len(matrix[0])
    for row in matrix:
        if len(row) != row_length:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(element / div, 2) for element in row] for row in matrix]
