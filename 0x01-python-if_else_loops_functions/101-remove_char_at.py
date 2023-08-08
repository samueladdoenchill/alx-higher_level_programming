#!/usr/bin/python3

def remove_char_at(str, n):
    """
    Remove the character at the specified index from a string.

    :param str: The input string.
    :param n: The index of the character to remove.
    :return: A new string with the character at index 'n' removed.
    """
    strtmp = ""
    cont = 0

    for c in str:
        if cont == n:
            pass
        else:
            strtmp += c
        cont += 1

    return strtmp
