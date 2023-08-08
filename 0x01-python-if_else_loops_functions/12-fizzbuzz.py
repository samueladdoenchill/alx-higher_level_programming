#!/usr/bin/python3

def fizzbuzz():
    """
    Print numbers from 1 to 100 with specific rules.

    Print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and
    "FizzBuzz" for numbers divisible by both 3 and 5. Otherwise, print
    the number itself. Each value is separated by a space.

    :return: None
    """
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end=" ")
        elif num % 3 == 0:
            print("Fizz", end=" ")
        elif num % 5 == 0:
            print("Buzz", end=" ")
        else:
            print(num, end=" ")
