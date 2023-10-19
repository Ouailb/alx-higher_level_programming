#!/usr/bin/python3

""" class square inherits from rectangle """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square  """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialization a Square"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        """ Update attributes """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attrs):
                    setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    @property
    def size(self):
        """
        Getter method for the size of the Square.

        Returns:
            int: The size of the Square.
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter method for the size of the Square.

        Args:
            value (int): The size value to be assigned.
        """
        self.width = value
        self.height = value

    def to_dictionary(self):
        """ Return a dictionary representation of the Rectangle """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
