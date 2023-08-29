#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Defines a node in a singly-linked list."""

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data of the Node."""
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represent a singly-linked list."""

    def __init__(self):
        """Initalize a new SinglyLinkedList isnatnce"""
        self.__head = None

    def sorted_insert(self, value):
        """Put a new Node to the SinglyLinkedList.

        Args:
            value (Node): The new Node.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            current_node = self.__head
            while (current_node.next_node is not None and
                    current_node.next_node.data < value):
                current_node = current_node.next_node
            new.next_node = current_node.next_node
            current_node.next_node = new

    def __str__(self):
        """Define print() representation of a SinglyLinkedList."""
        values = []
        current_node = self.__head
        while current_node is not None:
            values.append(str(current_node.data))
            current_node = current_node.next_node
        return ('\n'.join(values))
