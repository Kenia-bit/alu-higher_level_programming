#!/usr/bin/python3
"""A class MyList that inherits from list and adds print_sorted method."""


class MyList(list):
    """A subclass of list with a method to print the list in ascending order."""

    def print_sorted(self):
        """Prints the list in ascending order without modifying the original list."""
        print(sorted(self))
