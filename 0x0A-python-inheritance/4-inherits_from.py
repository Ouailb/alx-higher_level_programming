#!/usr/bin/python3
"""
    Check if an object is an instance of a class that inherited (directly or
    indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
    obj: Any object to be checked.
    a_class: The class to check against.

    Returns:
    True if obj is an instance of a class derived from a_class;
    otherwise, False.
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
