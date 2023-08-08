#!/usr/bin/python3

# Print characters in reverse order from 'z' to 'a'
# Convert lowercase letters to uppercase for odd ASCII values
# Print each character without a newline

for i in range(122, 96, -1):
    if i % 2 != 0:
        # Convert ASCII value to char and subtract 32 to convert to uppercase
        print("{:c}".format(i - 32), end='')
    else:
        # Convert ASCII value to char (no change for even values)
        print("{:c}".format(i), end='')
