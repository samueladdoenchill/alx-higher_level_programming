#!/usr/bin/python3

"""
A program that imports functions from a calculator module,
performs mathematical operations, and displays the results.
"""

if __name__ == "__main__":
    # Import functions from the calculator_1 module
    from calculator_1 import add, sub, mul, div

    # Define operands
    a = 10
    b = 5

    # Perform addition and display the result
    print("{} + {} = {}".format(a, b, add(a, b)))

    # Perform subtraction and display the result
    print("{} - {} = {}".format(a, b, sub(a, b)))

    # Perform multiplication and display the result
    print("{} * {} = {}".format(a, b, mul(a, b)))

    # Perform division and display the result
    print("{} / {} = {}".format(a, b, div(a, b)))
