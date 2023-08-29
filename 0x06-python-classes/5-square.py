#!/usr/bin/python3

class Square:
    def __init__(self, size):
        """
        Initialize a Square instance.

        Args:
            size (int): The size of the square's side.
        """
        self.size = size

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
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")