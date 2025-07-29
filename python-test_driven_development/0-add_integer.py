#!/usr/bin/python3
"""
This module defines a function that adds two integers.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats after validating and converting them.

    Args:
        a: First number (int or float).
        b: Second number (int or float), defaults to 98.

    Returns:
        int: The sum of a and b, casted to integers.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    for arg, name in ((a, 'a'), (b, 'b')):
        if not isinstance(arg, (int, float)):
            raise TypeError(f"{name} must be an integer")
        try:
            int(arg)
        except (ValueError, OverflowError):
            raise TypeError(f"{name} must be an integer")

    return int(a) + int(b)
