#!/usr/bin/python3
"""
This module defines a function that adds two integers.
The function validates input types and casts floats to integers.
"""

def add_integer(a, b=98):
    """
    Adds two integers or floats (which are casted to integers).
    
    Args:
        a (int or float): First number.
        b (int or float): Second number. Defaults to 98.
    
    Returns:
        int: The sum of the two integers.
    
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if isinstance(a, float):
        if a != a:  # NaN check
            raise TypeError("a must be an integer")
        a = int(a)
    elif not isinstance(a, int):
        raise TypeError("a must be an integer")

    if isinstance(b, float):
        if b != b:  # NaN check
            raise TypeError("b must be an integer")
        b = int(b)
    elif not isinstance(b, int):
        raise TypeError("b must be an integer")

    return a + b
