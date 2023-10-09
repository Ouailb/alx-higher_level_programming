#!/usr/bin/python3

"""
    Check if an object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance of, or if it is an instance of a class
    that inherited from, the specified class.

    Args:
    obj: Any object to be checked.
    a_class: The class to compare with.

    Returns:
    True if obj is an instance of a_class or inherits from it;
    otherwise, False.
    """
    return isinstance(obj, a_class)


a = 1
if is_kind_of_class(a, int):
    print("{} comes from {}".format(a, int.__name__))
if is_kind_of_class(a, float):
    print("{} comes from {}".format(a, float.__name__))
if is_kind_of_class(a, object):
    print("{} comes from {}".format(a, object.__name__))
