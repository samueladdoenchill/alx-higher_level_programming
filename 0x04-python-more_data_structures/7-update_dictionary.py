#!/usr/bin/python3

def update_dictionary(my_dict, key, value):
    """
    Update a dictionary by adding or updating a key-value pair.

    Args:
        my_dict (dict): The dictionary to be updated.
        key: The key to be added or updated.
        value: The value to be associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    my_dict[key] = value  # Add or update the key-value pair
    return my_dict  # Return the updated dictionary
