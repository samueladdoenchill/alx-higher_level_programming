#!/usr/bin/python3

# Entry point of the script
if __name__ == "__main__":
    import sys

    # Check the number of command-line arguments
    if len(sys.argv) == 1:
        # No arguments provided
        print("{} arguments.".format(len(sys.argv) - 1))
    elif len(sys.argv) == 2:
        # One argument provided
        print("{} argument:".format(len(sys.argv) - 1))
    else:
        # More than one argument provided
        print("{} arguments:".format(len(sys.argv) - 1))

    # Print the command-line arguments
    for i in range(len(sys.argv)):
        if i == 0:
            continue  # Skip the script name itself
        print("{:d}: {:s}".format(i, sys.argv[i]))
