#!/usr/bin/python3
"""Defines BaseGeometry, Rectangle, and Square classes."""


class BaseGeometry:
    """A base class for geometry."""

    def area(self):
        """Raises an Exception."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value is a positive integer."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """Defines a rectangle."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area."""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Defines a square, inheriting from Rectangle."""

    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size  # private, no getter or setter

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2


# Test case (like 10-main.py)
if __name__ == "__main__":
    s = Square(13)
    print(s)
    print(s.area())
