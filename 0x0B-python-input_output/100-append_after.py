#!/usr/bin/python3

""" Function that appends a line """


def append_after(filename="", search_string="", new_string=""):
    """ Appends a new line when a string is found """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
