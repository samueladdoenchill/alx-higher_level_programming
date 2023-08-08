#!/usr/bin/python3

def print_last_digit(number):
    '''Prints the last digit of the input number and returns its value.'''

    if number < 0:
        number = number * -1

    last_digit = number % 10
    print("{}".format(last_digit), end="")

    return last_digit
