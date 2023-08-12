#!/usr/bin/python3

"""
A program that displays the sum of all command-line arguments.
"""

if __name__ == "__main__":
    import sys

    total_sum = 0

    for arg in sys.argv[1:]:
        total_sum += int(arg)

    print("Sum of all arguments: {}".format(total_sum))
