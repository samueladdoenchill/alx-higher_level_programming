#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    """
    Return a set containing elements that are present in either
    set_1 or set_2, but not in both.

    Args:
        set_1 (set): The first input set.
        set_2 (set): The second input set.

    Returns:
        set: A set containing the symmetric difference of set_1 and set_2.
    """
    return set_1 ^ set_2
