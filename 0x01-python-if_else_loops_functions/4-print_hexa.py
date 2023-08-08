#!/usr/bin/python3
'''
Print numbers in the range in decimal and hexadecimal format
'''
for num in range(0, 99):
    print("{} = 0x{:x}".format(num, num))
