#!/usr/bin/python3

def islower(c):
    """
    Check if a character is a lowercase letter.

    :param c: The character to be checked.
    :return: True if 'c' is a lowercase letter, False otherwise.
    """
    if ord(c) >= 97 and ord(c) <= 122:
        return True
    return False
