#!/usr/bin/python3

"""  Module base geometry  """


class BaseGeometry:
    """
    A base class for geometry-related operations.
    """
    def area(self):
        """
        Raises:
        Exception: Indicates that the area() method is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.
        """
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
