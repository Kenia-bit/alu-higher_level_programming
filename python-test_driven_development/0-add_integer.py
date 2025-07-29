#!/usr/bin/python3
"""
Module for add_integer function.
Adds two integers or floats after type-checking and conversion.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats, returning the sum as an integer.

    Args:
        a: The first number (int or float).
        b: The second number (int or float), default is 98.

    Returns:
        The sum of a and b, casted to integers.

    Raises:
        TypeError: If a or b is not an integer or float,
                   or if it's a special float (NaN or inf).
    """
    for var, name in ((a, "a"), (b, "b")):
        if not isinstance(var, (int, float)):
            raise TypeError(f"{name} must be an integer")
        if isinstance(var, float):
            if var != var or var == float("inf") or var == float("-inf"):
                raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
