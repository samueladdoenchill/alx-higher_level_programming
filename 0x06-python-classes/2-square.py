#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square's side.
                        Defaults to 0 if not provided.
        
        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is negative.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size