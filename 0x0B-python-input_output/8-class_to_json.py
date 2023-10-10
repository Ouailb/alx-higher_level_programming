#!/usr/bin/python3

""" object with a simple data structure."""


def class_to_json(obj):
    """Returns a dictionary description of an object """
    if hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        return obj.__str__()
