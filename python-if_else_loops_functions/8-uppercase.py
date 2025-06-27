#!/usr/bin/python3
def uppercase(str):
    str = str if isinstance(str, str) else str.__str__()
    result = ""

    for char in str:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char

    print("{}".format(result))
