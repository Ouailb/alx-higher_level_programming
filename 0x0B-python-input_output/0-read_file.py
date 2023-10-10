#!/usr/bin/python3

"""Reads a text file (UTF8) and prints it to stdout."""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")

    # with open(filename, 'r', encoding="utf-8") as f:
    # read_data = f.read()

    #  print(read_data, end='')

    # print(f.read(), end="")
