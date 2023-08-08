#!/usr/bin/python3

def uppercase(str):
    '''Prints the input string in uppercase followed by a new line.'''
    result = ""

    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            result += chr(ord(c) - 32)
        else:
            result += c

    print("{}".format(result))
