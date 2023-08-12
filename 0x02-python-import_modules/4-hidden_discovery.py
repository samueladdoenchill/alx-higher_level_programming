#!/usr/bin/python3

if __name__ == "__main__":
    # Import the hidden_4 module
    import hidden_4

    # Get a list of all attributes in the hidden_4 module
    all_dir = dir(hidden_4)

    # Substring to avoid in attribute names
    avoid = "__"

    # Iterate through the attributes and print those not containing "avoid"
    for i in range(0, len(all_dir)):
        if avoid not in all_dir[i]:
            print(all_dir[i])  # Print the attribute name
