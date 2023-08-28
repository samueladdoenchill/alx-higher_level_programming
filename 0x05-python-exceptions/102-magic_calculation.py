#!/usr/bin/python3

# Define a function named magic_calculation that takes two arguments: a and b
def magic_calculation(a, b):
    result = 0

    for i in range(1, 3):
        try:

            if i > a:

                raise Exception('Too far')

            result = result + (a ** b) / i
        except Exception as e:
            result = b + a
            break

    return result
