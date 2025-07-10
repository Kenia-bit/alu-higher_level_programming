#!/usr/bin/python3
"""A class MyList that inherits from list."""


class MyList(list):
    """A subclass of list with a method to print the list in ascending order."""

    def print_sorted(self):
        """Prints a sorted version of the list (ascending), does not modify the original."""
        print(sorted(self))
