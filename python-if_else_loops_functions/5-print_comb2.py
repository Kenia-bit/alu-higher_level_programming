#!/usr/bin/python3
for i in range(0, 100):
    sep = ", " if i < 99 else "\n"
    print("{:02}".format(i), end=sep)
