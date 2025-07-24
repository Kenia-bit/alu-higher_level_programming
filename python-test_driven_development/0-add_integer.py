#!/usr/bin/python3
"""
This module provides a function `add_integer`
that adds two integers or floats after casting them to integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after casting to integers.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), defaults to 98.

    Returns:
        int: The sum of a and b casted to integers.

    Raises:
        TypeError: If either a or b is not an int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
