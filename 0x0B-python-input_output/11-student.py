#!/usr/bin/python3


Student = __import__('10-student').Student

def reload_from_json(self, json):
        """replaces all attributes of the Student"""
        for key, value in json.items():
            setattr(self, key, value)
