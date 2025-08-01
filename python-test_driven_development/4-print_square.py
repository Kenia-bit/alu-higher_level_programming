#!/usr/bin/python3
#!/usr/bin/python3
"""
>>> print_square(4)
####
####
####
####

>>> print_square(1)
#

>>> print_square(0)

>>> print_square(-1)
Traceback (most recent call last):
...
ValueError: size must be >= 0

>>> print_square(3.5)
Traceback (most recent call last):
...
TypeError: size must be an integer

>>> print_square("3")
Traceback (most recent call last):
...
TypeError: size must be an integer
"""

def print_square(size):
    # your function code here

"""
Module that defines a function to print a square made of '#' characters.
"""


def print_square(size):
    """
    Prints a square of '#' characters with the given size.

    Args:
        size (int): The length of each side of the square.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
