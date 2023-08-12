#!/usr/bin/python3


if __name__ == "__main__":
    # Import the add function from the add_0 module
    from add_0 import add

    # Define operands
    a = 1
    b = 2

    # Calculate the answer using the add function
    answer = add(a, b)

    # Print the addition equation and the answer
    print("{} + {} = {}".format(a, b, answer))
