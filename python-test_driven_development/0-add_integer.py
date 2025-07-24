#!/usr/bin/python3
"""
This module provides a function for adding two integers.
"""

def add_integer(a, b=98):
    """
    Adds two numbers, ensuring they are integers.

    Args:
        a (int or float): First number.
        b (int or float): Second number (default is 98).

    Returns:
        int: The sum of a and b, casted to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")

    # Handle NaN and float overflow safely
    try:
        a = int(a)
    except (ValueError, TypeError):
        raise TypeError("a must be an integer")

    try:
        b = int(b)
    except (ValueError, TypeError):
        raise TypeError("b must be an integer")

    return a + b
