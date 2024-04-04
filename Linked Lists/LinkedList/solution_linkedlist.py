# Author: Joel W. Prebish
# Creation Date: 03/01/2024
'''
This file contains solutions for LinkedList project.
Please only take a look after you gave it your best shot.
'''
class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class LinkedList():
    def __init__(self, head: Node=None, tail: Node=None):
        self.head = head
        self.tail = tail
    
    def insert_head(self, key):
        if(key is None): return
        node = Node(key, self.head)
        if(self.head is None):
            self.head = self.tail = node
        else: 
            self.head = node

    def insert_tail(self, key):
        if(key is None): return
        node = Node(key)
        if(self.head is None): 
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def remove_head(self):
        if self.head is self.tail: 
            self.head = self.tail = None
        else:
            self.head = self.head.next
    
    def remove_tail(self):
        if(self.head is self.tail):
            self.head = self.tail = None
        else:   
            curr: Node = self.head
            while(curr.next != self.tail):
                curr = curr.next
            curr.next = None
            self.tail = curr

    def remove(self, key):
        if(self.head is None or key is None):
            pass
        elif(self.head.data == key):
            self.remove_head()
        elif(self.tail.data == key):
            self.remove_tail()
        else:
            curr: Node = self.head
            while(curr.next):
                if(curr.next.data == key):
                    curr.next = curr.next.next
                    return
                curr = curr.next

    def search(self, key) -> Node:
        curr: Node = self.head
        while(curr and curr.data != key):
            curr = curr.next
        return curr

    def __str__(self) -> str:
        if(self.head is None): return "List is empty."
        string = "Head -> "
        curr: Node = self.head
        while(curr):
            if(curr.next is None):
                string += f"[{curr.data}]"
            else: 
                string += f"[{curr.data}] -> "
            curr = curr.next
        string += " -> Tail"
        return string