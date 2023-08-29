#!/usr/bin/python3

class Square:
    """Initialize a Square instance."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the square's side.
            Defaults to 0 if not provided.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size