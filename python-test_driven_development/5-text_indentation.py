#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    i = 0
    length = len(text)
    while i < length:
        print(text[i], end="")
        if text[i] in ['.', '?', ':']:
            print()  # first newline
            print()  # second newline (total two new lines)
            i += 1
            while i < length and text[i] == ' ':
                i += 1
            # Avoid extra blank line after last punctuation
            if i >= length:
                break
            continue
        i += 1
