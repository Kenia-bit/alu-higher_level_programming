#!/usr/bin/python3
"""
Module that defines add_integer(a, b=98)
Adds two integers or floats after validation.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after validating types.
    Args:
        a: first number (int or float)
        b: second number (int or float)
    Returns:
        int: sum of the two numbers as integers
    Raises:
        TypeError: if a or b is not int or float,
                   or is NaN or infinity
    """
    for var, name in ((a, "a"), (b, "b")):
        if not isinstance(var, (int, float)):
            raise TypeError(f"{name} must be an integer")
        # check for NaN or infinity (float values that can't be cast to int)
        if isinstance(var, float):
            if var != var or var in (float('inf'), float('-inf')):
                raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
