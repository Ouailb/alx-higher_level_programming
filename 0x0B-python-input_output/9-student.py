#!/usr/bin/python3

""" Module that defines the class Student """


class Student:

    """ Class to create student instances """

    def __init__(self, first_name, last_name, age):
        """ Special method to initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Method that returns directory description """
        student_json = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
        return student_json
