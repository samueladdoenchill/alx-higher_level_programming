#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square's side. Defaults to 0 if not provided.
            position (tuple): The position of the square. Defaults to (0, 0) if not provided.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Get the current size of the square.

        Returns:
            int: The current size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The size to set for the square's side.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is negative.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the current position of the square.

        Returns:
            tuple: The current position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The position to set for the square.

        Raises:
            TypeError: If the provided value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The calculated area of the square.
        """
        return (self.__size * self.__size)

    def my_print(self):
        """
        Print the square with the '#' character.
        """
        if self.__size == 0:
            print("")
            return

        [print("") for i in range(0, self.__position[1])]
        for i in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")