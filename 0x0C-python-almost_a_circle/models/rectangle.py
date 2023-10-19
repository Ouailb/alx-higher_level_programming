#!/usr/bin/python3

""" Rectangle class module """


from models.base import Base


class Rectangle(Base):

    """ Rectangle class that inherits from Base """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ Initializes a Rectangle instance """

        super().__init__(id)  # Call the superclass constructor with id

        # Use setters to validate and assign the attributes
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ Getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ Setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ Getter for x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Setter for x """
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Getter for y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Setter for y """
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):

        """ Calculate and return the area of the rectangle """
        return self.__width * self.__height

    # def display(self):
    #    """ Display the rectangle with '#' characters """
    #    for _ in range(self.__height):
    #        print("#" * self.__width)

    def display(self):
        """ Display the rectangle with '#' characters,
        accounting for x and y """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """ String representation of the Rectangle instance """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    # def update(self, *args):
    #    """ Update attributes with no-keyword arguments """
    #    if args:
    #        if len(args) >= 1:
    #            self.id = args[0]
    #        if len(args) >= 2:
    #            self.width = args[1]
    #        if len(args) >= 3:
    #            self.height = args[2]
    #         if len(args) >= 4:
    #             self.x = args[3]
    #        if len(args) >= 5:
    #             self.y = args[4]

    def update(self, *args, **kwargs):
        """ Update attributes with a combination of
        positional and keyword arguments """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
               if i < len(attrs):
                   setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
               setattr(self, key, value)
