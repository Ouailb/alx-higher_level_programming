#!/usr/bin/python3
"""Returns the JSON representation of an object as a string."""


import json


def to_json_string(my_obj):

    """Returns the JSON representation of an object as a string."""

    return json.dumps(my_obj)

# Test the function
"""
if __name__ == "__main__":

    my_list = [1, 2, 3]
    s_my_list = to_json_string(my_list)
    print(s_my_list)
    print(type(s_my_list))
    print("------------")
    my_dict = {
        'id': 12,
        'name': "John",
        'places': [ "San Francisco", "Tokyo" ],
        'is_active': True,
        'info': {
            'age': 36,
            'average': 3.14
        }
    }
    s_my_dict = to_json_string(my_dict)

    print(s_my_dict)
    print("------------")
    print(type(s_my_dict))
    print("------------")

    try:
        my_set = {'id': 00,'name': "oy" }
        print(to_json_string(my_set))
        print("------------")
        print(type(to_json_string(my_set)))
    except Exception as e:
        print("[{}] {}".format(e.__class__.__name__, e))
"""