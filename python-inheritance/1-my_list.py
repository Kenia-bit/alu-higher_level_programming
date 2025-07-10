#!/usr/bin/python3
"""A class MyList that inherits from list and adds a method to print sorted list."""


class MyList(list):
    """A subclass of list with a method to print the list in ascending order."""

    def print_sorted(self):
        """Prints the list in ascending sorted order (without modifying the original)."""
        print(sorted(self))
