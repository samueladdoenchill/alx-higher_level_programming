#!/usr/bin/python3

# Define a function that prints integers from a list
def print_list_integers(my_list=[]):
    # Iterate through the elements in the list
    for int_value in my_list:
        # Print each integer element
        print("{:d}".format(int_value))
