#!/usr/bin/python3

def simple_delete(my_dict, key=""):
    """
    Delete a key from a dictionary if it exists.

    Args:
        my_dict (dict): The dictionary from which to delete the key.
        key (str): The key to be deleted from the dictionary.

    Returns:
        dict: The modified dictionary after deleting the specified key (if found).
    """
    if key in my_dict:  # Check if the key exists in the dictionary
        del my_dict[key]  # Delete the key-value pair
    return my_dict  # Return the modified dictionary
