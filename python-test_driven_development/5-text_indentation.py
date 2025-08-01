#!/usr/bin/python3
"""Module that defines text_indentation function."""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: '.', '?', and ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    i = 0
    while i < len(text):
        print(text[i], end="")
        if text[i] in special_chars:
            print("\n")
            i += 1
            # Skip all spaces after punctuation
            while i < len(text) and text[i] == ' ':
                i += 1
            continue
        i += 1
