#!/usr/bin/python3

# Entry point of the script
if __name__ == "__main__":
    # Import functions from calculator_1 module
    from calculator_1 import add, sub, mul, div

    # Define operands
    a = 10
    b = 5

    # Perform addition and print the result
    print("{:n} + {:n} = {:n}".format(a, b, add(a, b)))

    # Perform subtraction and print the result
    print("{:n} - {:n} = {:n}".format(a, b, sub(a, b)))

    # Perform multiplication and print the result
    print("{:n} * {:n} = {:n}".format(a, b, mul(a, b)))

    # Perform division and print the result
    print("{:n} / {:n} = {:n}".format(a, b, div(a, b)))
