#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Sort the keys alphabetically and iterate through them
    for key in sorted(a_dictionary.keys()):
        value = a_dictionary[key]
        print("{}: {}".format(key, value))
