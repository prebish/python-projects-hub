# Author: Joel W. Prebish
# Creation Date: 04/04/2024
'''
This file contains the stack module for TowersOfHanoi project.
'''
class Stack:
    
    def __init__(self):
        """
        Initialize a new instance of the Stack class.

        This method creates an empty stack. A stack is a data structure that follows the Last In, First Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed. This implementation uses a Python list to store the elements of the stack, allowing dynamic resizing and efficient access to the top element.
        """
        self._items = []

    def push(self, element):
        """Insert an object at the top of the stack."""
        self._items.append(element)

    def pop(self):
        """Removes the top element of the stack."""
        if not self.empty():
            return self._items.pop()

    def peek(self):
        """Returns the top element without removing it from the stack. None if the stack is empty."""
        if not self.empty():
            return self._items[-1]
        return None

    def empty(self):
        """Returns True if the stack is empty, False otherwise."""
        return len(self._items) == 0
    
    def clear(self):
        """Removes all elements from the stack."""
        self._items.clear()
    
    def __len__(self):
        """Returns the length of the stack."""
        return len(self._items)
    
    def __iter__(self):
        """Iterates from the top of the stack to the bottom."""
        return reversed(self._items)

    def __str__(self):
        return str(list(self))