#!/usr/bin/python3
# Write a function that prints an integer with "{:d}".format().


def safe_print_integer(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:  # changed the except block to be generic
        return False
