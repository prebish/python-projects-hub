# Author: Joel W. Prebish
# Creation Data: 03/01/2024
'''
Methods are already in order they should be implemented.
The more generalized the method name seems, the more generalized the implementation tends to be.
Think about how the methods you've already implemented can help you in implementing others.
'''

#NOTE DO NOT MODIFY THIS CLASS
class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class CircularDLL():
    def __init__(self, head: Node=None, tail: Node=None):
        self.head: Node = head
        self.tail: Node = tail
        #TODO additional fields as needed... HINT HINT
    
    # indicates the list is empty or not
    def empty(self) -> bool:
        #TODO complete implementation
        raise NotImplementedError("empty not implemented.")
    
        return None 

    # adds a node to front of the list
    def insert_head(self, key):
        #TODO complete implementation
        raise NotImplementedError("insert_head not implemented.")
    
        return

    # adds a node to end of the list
    def insert_tail(self, key):
        #TODO complete implementation
        raise NotImplementedError("insert_tail not implemented.")
    
        return

    # removes a node from front of list
    def remove_head(self):
        #TODO complete implementation
        raise NotImplementedError("remove_head not implemented.")
    
        return

    # removes node from end of list 
    def remove_tail(self):
        #TODO complete implementation
        raise NotImplementedError("remove_tail not implemented.")
    
        return
    
    # traverses the list looking for a node containing 'key'
    # returns node containing the key
    def search(self, key) -> Node:
        #TODO complete implementation
        raise NotImplementedError("search not implemented.")
    
        return None

    # what could simplify this?
    def contains(self, key) -> bool:
        #TODO complete implementation
        raise NotImplementedError("contains not implemented.")
    
        return None

    # traverses the list and removes node containing 'key'
    def remove(self, key):
        #TODO complete implementation
        raise NotImplementedError("remove not implemented.")

        return

    # NOTE must run faster than 0.01 seconds
    def size(self) -> int:
        #TODO complete implementation
        raise NotImplementedError("size not implemented.")
    
        return None

    # removes all nodes from the list and
    # ensures list size is set back to 0
    def clear(self):
        #TODO complete implementation
        raise NotImplementedError("clear not implemented.")
    
        return None

    # must return copy of list with
    # original list still in tact
    # returns a CDLL containing 1 node for 
    # every unique element. no duplicates.
    def set(self) -> 'CircularDLL':
        #TODO complete implementation
        raise NotImplementedError("set not implemented.")
    
        return None
        
    #NOTE this one is already completed for you.
    # its an override method. simply do 'print(list)'
    def __str__(self) -> str:
        if(self.empty()): return "List is empty."
        string = f"]-[{self.tail.data}] <- Head -> "
        curr: Node = self.head
        while(curr):
            if(curr.next is None):
                string += f"[{curr.data}]"
            else: string += f"[{curr.data}]-"
            curr = curr.next
            if curr is self.head: break
        string += f"\b <- Tail -> [{self.head.data}]-[ ..."
        return string
    