#!/usr/bin/python3
"""A script that appends a string to a file"""


def append_after(filename="", search_string="", new_string=""):
    """A function that appends a string to a file after the occurence
        of a particular string
        parameters:
            filename: the name of the file
            search_string: the string after which appending occurs
            new_string: the new string to be appended
    """
    lenght = len(search_string)
    with open(filename, "r+") as f:
        content = f.readlines()
        f.truncate(0)
        f.close
        f = open(filename, "a")
        for line in content:
            if search_string in line:
                f.write(line)
                f.write(new_string)
            else:
                f.write(line)
