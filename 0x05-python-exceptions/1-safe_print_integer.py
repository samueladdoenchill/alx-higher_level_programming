#!/usr/bin/python3

# Define a function named safe_print_integer
# that takes one argument:
# value (any type, but expected to be an integer)
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError):
        return False
    else:
        return True
