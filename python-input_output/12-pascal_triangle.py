#!/usr/bin/python3
"""
Module that implements Pascal's Triangle generation.
"""


def pascal_triangle(n):
    """
    Generate Pascal's triangle up to n rows.

    Args:
        n (int): Number of rows of the triangle to generate.

    Returns:
        list of list of int: Pascal's triangle represented as a list of rows,
        where each row is a list of integers.

    If n <= 0, returns an empty list.
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        row = [1]
        prev_row = triangle[i - 1]

        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])

        row.append(1)
        triangle.append(row)

    return triangle
