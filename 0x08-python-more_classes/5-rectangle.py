#!/usr/bin/python3

""" Defines a Rectangle class """


class Rectangle:
    """ First implementation of the class """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ retrieve the rectangle's width """
        return self.__width

    @width.setter
    def width(self, value):
        """ set the width """
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ get the rectangle's height """
        return self.__height

    @height.setter
    def height(self, value):
        """ set the rectangle's height """
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.width * self.height

    def perimeter(self):
        """ returns the rectangle perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__width + self.__height)

    def __str__(self):
        """ Returns the informal string representaion
        of the rectangle """

        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            result = ""
            for _ in range(self.__height):
                result += '#' * self.__width + '\n'
            return result.rstrip()

    def __repr__(self):
        """should return a string representation of the rectangle
        to be able to recreate a new instance by using eval() """

        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        print("Bye rectangle...")
