#!/usr/bin/python3
"""A class Rectangle that defines a rectangle."""
  

class Rectangle:
    """Defines a rectangle with width and height."""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    def __str__(self):
        """Returns a printable representation using the print_symbol."""
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for _ in range(self.height):
            result += str(self.print_symbol) * self.width + "\n"
        return result.rstrip()

    def __repr__(self):
        """Returns an official string representation for eval()."""
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Called when an instance is deleted."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates area of the rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Calculates perimeter of the rectangle."""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def __eq__(self, other):
        """Compares rectangles by area using ==."""
        if isinstance(other, Rectangle):
            return self.area() == other.area()
        return False

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Returns the rectangle with the greater or equal area."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2


# Optional test block (only runs when executed directly)
if __name__ == "__main__":
    r1 = Rectangle(8, 4)
    r2 = Rectangle(4, 8)
    print(r2 == Rectangle.bigger_or_equal(r1, r2))  # Expected: False
