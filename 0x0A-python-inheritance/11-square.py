#!/usr/bin/python3

"""Defines a subclass Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square that inherits from Rectangle"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """ str function to print with/height """
        return '[Square] ' + str(self.__size) + '/' + str(self.__size)
