#!/usr/bin/env python3
"""Defines a Square class with size validation and area method."""


class Square:
    """Represents a square with a validated size and area calculation."""

    def __init__(self, size=0):
        """Initializes a new Square.

        Args:
            size (int): The size of the square.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2
