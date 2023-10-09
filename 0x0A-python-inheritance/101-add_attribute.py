#!/usr/bin/python3
""" adds attributes to objects """


def add_attribute(obj, attr_name, attr_value):
    """
    Add a new attribute to an object if it's possible.
    """
    if hasattr(obj, '__dict__') or (
        hasattr(type(obj), '__slots__') and attr_name in type(obj).__slots__
    ):
        setattr(obj, attr_name, attr_value)
    else:
        raise TypeError("can't add new attribute")
