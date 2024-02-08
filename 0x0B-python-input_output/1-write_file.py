#!/usr/bin/python3

"""Writes a string to a text file (UTF8) """


def write_file(filename="", text=""):
    """ returns the number of characters written."""

    with open(filename, mode="w", encoding="utf-8") as file:
        nb_characters = file.write(text)
    return nb_characters

    # with open(filename, mode="w", encoding="utf-8") as file:
    #    nb_characters = file.write(text)
    # return nb_characters


    # with open(filename, 'w') as f:
    #    return f.write(text)


    # if filename == "" or type(filename) != str:
    #    return 0
    # counter = 0
    # with open(filename, 'r') as f:
    #   for line in f:
    #        counter += 1
    # return counter


# nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
# print(nb_characters)
