#!/usr/bin/env python3
"""
Module 2-square
Defines a Square class that inherits from Rectangle and customizes __str__.
"""

Rectangle = __import__('2-rectangle').Rectangle


class Square(Rectangle):
    """Represent a square using Rectangle."""

    def __init__(self, size):
        """Initialize a new Square.

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the print() and str() representation of the Square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
