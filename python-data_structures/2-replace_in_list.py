#!/usr/bin/python3


# function that replaces an element of a list at a specific position.
def replace_in_list(my_list, idx, element):
    count = len(my_list)
    if idx < 0:
        return my_list
    elif idx >= count:
        return my_list
    else:
        my_list[idx] = element
        return my_list
