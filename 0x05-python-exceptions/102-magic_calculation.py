#!/usr/bin/python3

# Define a function named magic_calculation that takes
# two arguments: a and b
def magic_calculation(a, b):
    modified_result = 0

    for modified_i in range(1, 3):
        try:
            if modified_i > a:
                raise Exception('Too far')

            modified_result += a ** b / modified_i
        except:
            modified_result = b + a
            break

        return modified_result
