#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    """
    Delete keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): The dictionary in which to perform the deletion.
        value: The value to be searched for and removed.

    Returns:
        dict: modified dictionary after removing keys with specified value.
    """
    while value in a_dictionary.values():
        for key, val in a_dictionary.items():
            if val == value:
                del a_dictionary[key]
                break
    return a_dictionary
