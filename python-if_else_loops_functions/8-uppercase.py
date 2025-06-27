#!/usr/bin/python3
def uppercase(str):
    strlen = len(str)
    if strlen == 0:
        print()  # Handle the empty string case
        return

    i = 0
    while i < strlen:
        char = ord(str[i])
        if char < 97 or char > 122:
            print("{}".format(chr(char)), end="" if i < strlen - 1 else "\n")
        else:
            char = char - 32
            print("{}".format(chr(char)), end="" if i < strlen - 1 else "\n")
        i += 1
