#!/usr/bin/python3

""" Print the list in ascending sorted order """


class MyList(list):
    """
        Print the list in ascending sorted order.
     """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.
        """
        print(sorted(self))
