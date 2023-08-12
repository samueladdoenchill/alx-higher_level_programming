#!/usr/bin/python3

if __name__ == "__main__":
    """Entry point of the script."""

    import sys

    # Initialize the total sum
    total = 0

    # Loop through command-line arguments and calculate the total
    for i in range(len(sys.argv) - 1):
        # Convert the argument to an integer and add to the total
        total += int(sys.argv[i + 1])

        # Print the current total
        print("{}".format(total))
