#!/usr/bin/python3
"""Module that defines the Square class."""


class Square:
    """Square class that validates size and calculates area."""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def integer_validator(self, name, value):
        """Validate that value is an int and > 0."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    def area(self):
        """Return area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return string representation: [Square] size/size"""
        return "[Square] {}/{}".format(self.__size, self.__size)
