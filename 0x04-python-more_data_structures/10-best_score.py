#!/usr/bin/python3

def best_score(my_dict):
    """
    Find the key with the highest value in the dictionary.

    Args:
        my_dict (dict): The dictionary containing key-value pairs.

    Returns:
        str: Key with highest value, or None if dict is empty.
    """
    if my_dict and len(my_dict):
        high_key = list(my_dict.keys())[0]
        for key in my_dict:
            if my_dict[key] > my_dict[high_key]:
                high_key = key
        return high_key
    return None
