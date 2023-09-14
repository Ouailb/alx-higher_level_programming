#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    # Calculate the symmetric difference (elements present in only one set)
    return (set_1 | set_2) - (set_1 & set_2)
