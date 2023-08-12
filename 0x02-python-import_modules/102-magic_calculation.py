#!/usr/bin/python3

def magic_calculation(a, b):
    # Import the add and sub functions from magic_calculation_102 module
    from magic_calculation_102 import add, sub

    # Check if a is less than b
    if a < b:
        c = add(a, b)

        # Loop from 4 to 5 and perform additions
        for i in range(4, 6):
            c = add(c, i)

        return c
    else:
        # Perform subtraction if a is not less than b
        return sub(a, b)
