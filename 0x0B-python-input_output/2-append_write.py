#!/usr/bin/python3

""" Appends a string to the end of a text file (UTF8) """


def append_write(filename="", text=""):
    """ returns the number of characters added """
    with open(filename, mode="a", encoding="utf-8") as file:
        nb_characters_added = file.write(text)
    return nb_characters_added


# ------------------------------------
# with open(filename, "a", encoding="utf-8") as f:
#        return f.write(text)
# ------------------------------------
# nb_characters_added = append_write("file_append.txt",
#                           "This School is so cool!\n")
# print(nb_characters_added)
