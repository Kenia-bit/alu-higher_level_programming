#!/usr/bin/python3
"""BaseGeometry module."""


class BaseGeometry:
    """Base class with area and integer_validator methods."""

    def area(self):
        """Raises exception for area not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates that value is a positive integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
