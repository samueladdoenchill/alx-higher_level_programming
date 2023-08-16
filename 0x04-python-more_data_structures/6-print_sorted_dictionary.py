#!/usr/bin/python3

def print_sorted_dictionary(my_dict):
    """
    Print the dictionary's keys and values in sorted order.

    Args:
        my_dict (dict): The dictionary to be printed.

    Returns:
        None
    """
    for key in sorted(my_dict.keys()):  # Iterate through keys in sorted order
        print("{:s}: {}".format(key, my_dict[key]))  # Print key and value
