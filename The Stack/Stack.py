class Stack():
    
    def __init__(self) -> None:
        """
        Initialize a new instance of the Stack class.

        This method creates an empty stack. A stack is a data structure that follows the Last In, First Out (LIFO) principle, meaning that the last element added to the stack is the first one to be removed. This implementation uses a Python list to store the elements of the stack, allowing dynamic resizing and efficient access to the top element.
        """
        self.__items = []

    def push(self, element):
        '''Insert an object at the top of the stack.'''
        self.__items.append(element)

    def pop(self):
        '''Removes the top element of the stack.'''
        if not self.empty():
            return(self.__items.pop())

    def peek(self):
        '''Returns the top element without removing it from the stack. None if no such element exists.'''
        return(self.__items[-1])
    
    def peek(self, index):
        '''Returns element in the specified index. None if no such element exists.'''
        if index < 0 or index >= len(self.__items):
            return None
        return self.__items[-(index + 1)]


    def empty(self):
        '''Returns True if the stack is empty, False otherwise.'''
        return (len(self.__items)==0)
    
    def clear(self):
        '''Removes all elements from the stack.'''
        self.__items.clear()
        return
    
    def reverse(self):
        '''Reverses the order of elements in the stack.'''
        self.__items.reverse()


    def __len__(self):
        '''Returns the length of the stack.'''
        return len(self.__items)
    
    def __iter__(self):
        '''Iterator for the stack.'''
        for item in reversed(self.__items):
            yield item
