#!/usr/bin/python3

def multiply_by_2(my_dict):
    """
    Multiply the values of a dictionary by 2 and create a new dictionary.

    Args:
        my_dict (dict): The dictionary containing key-value pairs.

    Returns:
        dict: A new dictionary with the same keys as 'my_dict' and values
              multiplied by 2.
    """
    return {key: value * 2 for key, value in my_dict.items()}
