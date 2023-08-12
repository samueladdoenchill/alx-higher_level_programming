#!/usr/bin/python3

# Import functions from calculator_1 module
from calculator_1 import add, sub, mul, div

def arg_calc(argv):
    # Calculate the number of arguments
    n = len(argv) - 1

    # Check if the correct number of arguments is provided
    if n != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    # Convert arguments to appropriate types
    a = int(argv[1])
    op = argv[2]
    b = int(argv[3])

    # Perform the calculation based on the operator
    if op == '+':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, add(a, b)))
    elif op == '-':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, sub(a, b)))
    elif op == '*':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, mul(a, b)))
    elif op == '/':
        print("{:d} {:s} {:d} = {:d}".format(a, op, b, div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

# Entry point of the script
if __name__ == "__main__":
    import sys
    # Call the arg_calc function with command-line arguments
    arg_calc(sys.argv)
