#!/usr/bin/python3
"""Module that defines Rectangle and Square classes without importing."""

class Rectangle:
    """Rectangle class with width and height validation."""

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """Validate that value is int and > 0."""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @property
    def height(self):
        """Height getter."""
        return self.__height

    def area(self):
        """Return area of rectangle."""
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Square class inherits from Rectangle."""

    def __init__(self, size):
        """Initialize Square with size validation."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size  # private attribute

    def area(self):
        """Return area of the square."""
        return self.__size ** 2

    def __str__(self):
        """Return string description of square."""
        return "[Square] {}/{}".format(self.width, self.height)
