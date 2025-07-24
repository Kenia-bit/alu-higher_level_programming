#!/usr/bin/python3
"""function that prints My name is <first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """say_my_name: function that prints strings fist and last names
        arguments
            first_name:(string) the first name to be printed
            last_name:(string) the last name to be printed
        Exceptions
            raised: TypeError exception is raised if any argument is not
                    a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
