# Author: Joel W. Prebish
# Creation Data: 03/01/2024
'''
This file contains solutions for DoublyLL project.
Please only take a look after you gave it your best shot.
'''

class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoublyLL():
    def __init__(self, head: Node=None, tail: Node=None):
        self.head = head
        self.tail = tail
        self.__size = 0 #NOTE '__' means this var can't be accessed outside this file.
    
    def empty(self) -> bool:
        return bool(self.head is None) 

    def insert_head(self, key):
        if(key is None): return
        node = Node(key, None, self.head)
        if(self.empty()):
            self.head = self.tail = node
        else:
            self.head.prev = node
            self.head = node
        self.__size+=1

    def insert_tail(self, key):
        if(key is None): return
        node = Node(key, self.tail)
        if(self.empty()):
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.__size+=1

    def remove_head(self):
        if(self.head is self.tail):
            self.head = self.tail = None
        else:
            self.head.next.prev = None
            self.head = self.head.next
        if self.__size: self.__size-=1
    
    def remove_tail(self):
        if(self.head is self.tail):
            self.head = self.tail = None
        else:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            if(self.empty()): 
                self.head = self.tail = None
        if self.__size: self.__size-=1

    def search(self, key) -> Node:
        curr = self.head
        while(curr and curr.data != key):
            curr = curr.next
        return curr

    def contains(self, key) -> bool:
        return bool(self.search(key))

    def remove(self, key):
        if(key is None or self.empty()):
            pass
        elif(self.head.data == key):
            self.remove_head()
        elif(self.tail.data == key):
            self.remove_tail()
        else:
            curr: Node = self.search(key)
            if curr is None: return
            prev = curr.prev; next = curr.next
            if(curr.data == key):
                prev.next = next
                next.prev = prev
                self.__size-=1

    def size(self) -> int:
        return self.__size

    def __str__(self) -> str:
        string = "Head -> "
        curr: Node = self.head
        while(curr):
            if(curr.next is None):
                string += f"[{curr.data}]"
            else: string += f"[{curr.data}]-"
            curr = curr.next
        string += " <- Tail"
        return string