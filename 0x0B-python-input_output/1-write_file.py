#!/usr/bin/python3

"""Writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ returns the number of characters written."""

    with open(filename, mode="w", encoding="utf-8") as file:
        nb_characters = file.write(text)
    return nb_characters


# nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# print(nb_characters)
