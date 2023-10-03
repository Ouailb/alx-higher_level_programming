#!/usr/bin/python3
"""class Rectangle"""


class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """ Instantiation with optional width and height"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width"""
        return self.__width

    @property
    def height(self):
        """hight"""
        return self.__height

    @width.setter
    def width(self, value):
        """width error"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """height error"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
