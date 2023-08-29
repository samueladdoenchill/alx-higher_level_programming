#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Defines a square instance."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square instance.

        Args:
            size (int): The lenght of the square
            position (int, int): The cordinates of the square
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Get the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Get the current position of the square."""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the calculated area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print square with # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for row in range(0, self.__position[1])]
        for row in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            print("")

    def __str__(self):
        """Define print() representation of a Square."""
        if self.__size != 0:
            [print("") for row in range(0, self.__position[1])]
        for row in range(0, self.__size):
            [print(" ", end="") for j in range(0, self.__position[0])]
            [print("#", end="") for k in range(0, self.__size)]
            if row != self.__size - 1:
                print("")
        return ("")
