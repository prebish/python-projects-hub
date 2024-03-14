 # Author: Joel W. Prebish
# Creation Data: 03/01/2024
'''
This file contains solutions for CDLL.py
'''

class Node():
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class CircularDLL():
    def __init__(self, head: Node=None, tail: Node=None):
        self.head = head
        self.tail = tail
        self.__size = 0
    
    def empty(self) -> bool:
        return bool(self.head is None) 

    def insert_head(self, key):
        if(key is None): return

        node = Node(key, self.tail, self.head)
        if(self.head is self.tail is None):
            self.head = self.tail = node
            node.prev = node.next = node
        else:
            self.head.prev = node
            self.tail.next = node
            self.head = node
        self.__size+=1
        
    def insert_tail(self, key):
        if(key is None): return

        node = Node(key, self.tail, self.head)
        if(self.head is self.tail is None):
            self.head = self.tail = node
            node.prev = node.next = node
        else:
            self.head.prev = node
            self.tail.next = node
            self.tail = node
        self.__size+=1

    def remove_head(self):
        if(self.head is self.tail):
            self.head = self.tail = None
        else:
            self.tail.next = self.head.next
            self.head = self.head.next
            self.head.prev = self.tail
        if(self.__size): self.__size-=1
    
    def remove_tail(self):
        if(self.head is self.tail):
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        if(self.__size): self.__size-=1

    def search(self, key) -> Node:
        curr = self.head
        while(curr):
            if curr.data == key:
                return curr
            curr = curr.next
            if curr is self.head: break
        return None

    def contains(self, key) -> bool:
        return bool(self.search(key))

    def remove(self, key):
        if(self.empty() or key is None): 
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

    def clear(self):
        self.head = self.tail = None
        self.__size = 0

    def set(self) -> 'CircularDLL':
        if(self.empty()): return CircularDLL()
        ul = CircularDLL()
        ul.insert_tail(self.head.data)
        curr = self.head.next

        while(curr != self.head):
            if not ul.contains(curr.data):
                ul.insert_tail(curr.data)
            curr = curr.next
        return ul  

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