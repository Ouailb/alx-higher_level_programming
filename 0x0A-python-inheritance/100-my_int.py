#!/usr/bin/python3
""" A class that inherits from int """


class MyInt(int):
    """ It overrides the == and != operators """

    def __eq__(self, other):
        """ Override the == operator """
        return super().__ne__(other)
        # return int(str(self)) != other

    def __ne__(self, other):
        """ Override the != operator """
        return super().__eq__(other)
        # return int(str(self)) == other
