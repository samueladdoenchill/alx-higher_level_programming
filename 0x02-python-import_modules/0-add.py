#!/usr/bin/python3

if __name__ == "__main__":
    """Entry point of the script."""

    # Import the add function from the add_0 module.
    from add_0 import add

    # Define variables for the operands.
    a = 1
    b = 2

    # Calculate the sum using the add function and print the result.
    print("{} + {} = {}".format(a, b, add(a, b)))
