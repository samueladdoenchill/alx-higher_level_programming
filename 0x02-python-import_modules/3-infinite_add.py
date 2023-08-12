#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    total_sum = 0

    if len(sys.argv) == 1:
        print("{:d}".format(total_sum))
    else:
        for arg in sys.argv[1:]:
            total_sum += int(arg)
        print("{:d}".format(total_sum))
