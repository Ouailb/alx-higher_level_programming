#!/usr/bin/python3

""" Module that defines the class Student """


class Student:
    """ Class to create student instances """
    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Method that returns """
        if attrs is None:
            return self.__dict__.copy()
        else:
            result = {}
            for attr in attrs:
                if hasattr(self, attr):
                    result[attr] = getattr(self, attr)
            return result


    def reload_from_json(self, json):
        """replaces all attributes of the Student"""
        for key, value in json.items():
            setattr(self, key, value)
