# Author: Joel W. Prebish
# Creation Data: 03/01/2024
'''
DO NOT MODIFY
Try to implement insert_head() first, as multiple other tests depend on it.
To run these tests, use VS Code extensions or 'pytest Test_LL.py' in terminal.
'''
#region I M P O R T S
import pytest, time

# Your Impl
from doublyll import DoublyLL, Node
# Solution
from solution_doublyll import DoublyLL as Solution
#endregion

def test_empty():
    l = DoublyLL()
    assert l.empty(), "Observed: False || Expected: True"

    l.insert_head(0)
    assert not l.empty(), "Observed: False || Expected: True" 

def test_insert_head():
    
    # Adding object 'None' to empty list
    l = DoublyLL()
    l.insert_head(None)
    expected = f"head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Adding one object to empty list
    l.insert_head(0)
    expected = "head and tail should be the same object."
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(l.head is l.tail and l.tail.data == 0), f"Observed: {observed} || Expected: {expected}"

    # Adding multiple objects
    l = DoublyLL()
    l.insert_head(3); l.insert_head(2)
    l.insert_head(1); l.insert_head(0)
    expected = "head=0 tail=3"
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Head prev and next check
    expected = "head.prev=None, .next=1"
    observed = f"head.prev={l.head.prev}, .next={l.head.next.data}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Tail prev and next check
    expected = "tail.prev=2, .next=None"
    observed = f"tail.prev={l.tail.prev.data}, .next={l.tail.next}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

def test_insert_tail():
    l = DoublyLL()

    # Adding object 'None' to empty list
    l = DoublyLL()
    l.insert_tail(None)
    expected = f"head and tail should have the same address. Their data should be None."
    observed = f"l.head={l.head} tail={l.tail} "
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Adding one object to empty list
    l.insert_tail(0)
    expected = "head and tail should be the same object."
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(l.head is l.tail and l.head.data == 0), f"Observed: {observed} || Expected: {expected}"

    # Adding multiple objects
    l = DoublyLL()
    l.insert_tail(0); l.insert_tail(1)
    l.insert_tail(2); l.insert_tail(3)
    expected = "head=0 tail=3"
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Head prev and next check
    expected = "head.prev=None, .next=1"
    observed = f"head.prev={l.head.prev}, .next={l.head.next.data}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Tail prev and next check
    expected = "tail.prev=2, .next=None"
    observed = f"tail.prev={l.tail.prev.data}, .next={l.tail.next}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

# Dependencies: 
#   insert_head()
def test_remove_head():

    # On initialized list
    l = DoublyLL()
    l.remove_head()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Removing one element from list size 1
    l.insert_head(0)
    l.remove_head()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Head and Tail with list size 1
    l.insert_head(4)
    expected = "head and tail should have the same address. Their data should be 1"
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail and l.head.data == 4), f"Observed: {observed} || Expected: {expected}"
    expected = "tail.prev=None, .next=None"
    observed = f"tail.prev={l.tail.prev}, .next={l.tail.next}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Removing some from list
    l.insert_head(3); l.insert_head(2); l.insert_head(1); l.insert_head(0)
    l.remove_head(); l.remove_head(); l.remove_head()
    expected = "head=3 tail=4"
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(l.head.data == 3 and l.tail.data == 4), f"Observed: {observed} || Expected: {expected}"

    # Removing all from list
    l.remove_head(); l.remove_head()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Removing more than size of list 
    l.remove_head(); l.remove_head()
    l.remove_head(); l.remove_head()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

# Dependencies:
#   insert_head()
def test_remove_tail():

    # On initialized list
    l = DoublyLL()
    l.remove_tail()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Removing one element from list size 1
    l.insert_head(0)
    l.remove_tail()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Head and Tail with list size 1
    l.insert_head(4)
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail and l.head.data == 4), f"Observed: {observed} || Expected: {expected}"
    expected = "tail.prev=None, .next=None"
    observed = f"tail.prev={l.tail.prev}, .next={l.tail.next}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Removing some from list
    l.insert_head(3); l.insert_head(2); l.insert_head(1); l.insert_head(0)
    l.remove_tail(); l.remove_tail(); l.remove_tail()
    expected = "head=0 tail=1"
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(l.head.data == 0 and l.tail.data == 1), f"Observed: {observed} || Expected: {expected}"

    # Removing all from list
    l.remove_tail(); l.remove_tail()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Removing more than size of list 
    l.remove_tail(); l.remove_tail()
    l.remove_tail(); l.remove_tail()
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

# Dependencies:
#   insert_head()
#   insert_tail()
#   remove_head()
def test_search():
    l = DoublyLL()

    # Search end of list for 50
    for data in range(99):
        if data % 2 == 0: l.insert_head(data)
        else: l.insert_tail(data)

    node: Node = l.search(50)
    expected = "node.data=50"
    observed = f"node.data={node.data}"
    assert(node.data == 50), f"Observed: {observed} || Expected: {expected}"


    # Search for 50 in empty list
    for data in range(101): l.remove_head()
    node: Node = l.search(50)
    expected = "node is None"
    observed = f"node is {node}"
    assert(node is None), f"Observed: {observed} || Expected: {expected}"

def test_contains():

    # Single
    l = DoublyLL()
    l.insert_head(5)
    assert(l.contains(5) == True), "Observed: False || Expected: True"
    assert(l.contains(-1) == False), "Observed: True || Expected: False"

    # Many
    l.insert_head(4); l.insert_head(3); l.insert_head(2)
    l.insert_head(1); l.insert_head(0)
    assert(l.contains(0) == True), "Observed: False || Expected: True"
    assert(l.contains(3) == True), "Observed: False || Expected: True"
    assert(l.contains(-1) == False), "Observed: True || Expected: False"

# Dependencies:
#   insert_head()
def test_remove():
    
    # On empty list
    l = DoublyLL()
    l.remove(0)
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # On list with size 1 and calls to non existent elements
    l.remove("foo")
    l.insert_head(0)
    l.remove(0)
    l.remove("bar")
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

    # Last elements in list with size > 1
    l.insert_head(6); l.insert_head(5)
    l.insert_head(4); l.insert_head(3); l.insert_head(2)
    l.insert_head(1); l.insert_head(0)
    l.remove(6); l.remove(5)
    expected = "head=0 tail=4"
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(l.head.data == 0 and l.tail.data == 4), f"Observed: {observed} || Expected: {expected}"

    # Middle element in list size 5
    l.remove(2)
    expected = "head.next=1 next.next=3"
    observed = f"head.next={l.head.next.data} next.next={l.head.next.next.data}"
    assert(l.head.next.data == 1 and l.head.next.next.data == 3), f"Observed: {observed} || Expected: {expected}"

    # All but one element from list
    l.remove(3); l.remove(1); l.remove(0)
    expected = "head and tail should have the same address. Their data should be 4."
    observed = f"head={l.head.data} tail={l.tail.data}"
    assert(l.head is l.tail and l.head.data == 4), f"Observed: {observed} || Expected: {expected}"

    # Head and Tail with list size 1
    expected = "tail.prev=None, .next=None"
    observed = f"tail.prev={l.tail.prev}, .next={l.tail.next}"
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Keep removing past empty
    l.remove("foo")
    l.remove(4)
    l.remove("bar")
    l.remove(4)
    expected = "head and tail should have the same address. Their data should be None."
    observed = f"head={l.head} tail={l.tail}"
    assert(l.head is l.tail is None), f"Observed: {observed} || Expected: {expected}"

# Dependencies:
#   insert_head()
#   insert_tail()
def test_size_efficiency():
    l = DoublyLL()
    for _ in range(0, 999999):
        l.insert_head(-1)
        l.insert_tail(-1)

    start = time.time()
    _ = l.size()
    stop = time.time()
    actual = stop-start

    assert actual < 0.0001

# Dependencies:
#   insert_head()
#   remove_head()
def test_size_h():
    l = DoublyLL()

    # Insert 30 nodes
    for i in range(30):
        l.insert_head(i)
    observed = l.size()
    expected = 30
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Remove 15 nodes
    for i in range(15):
        l.remove_head()
    observed = l.size()
    expected = 15
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Remove passed empty
    for i in range(20):
        l.remove_head()
    observed = l.size()
    expected = 0
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

# Dependencies:
#   insert_tail()
#   remove_tail()
def test_size_t():
    l = DoublyLL()

    # Insert 30 nodes
    for i in range(20):
        l.insert_tail(i)
    observed = l.size()
    expected = 20
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Remove 15 nodes
    for i in range(15):
        l.remove_tail()
    observed = l.size()
    expected = 5
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Remove passed empty
    for i in range(20):
        l.remove_tail()
    observed = l.size()
    expected = 0
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

# Dependencies:
#   insert_head()
#   remove()
def test_size_r():
    l = DoublyLL()

    # Insert 30 nodes
    for i in range(20):
        l.insert_head(i)
    observed = l.size()
    expected = 20
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Remove 15 nodes
    for i in range(15):
        l.remove(i)
    observed = l.size()
    expected = 5
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Remove passed empty
    for i in range(15, 30):
        l.remove(i)
    observed = l.size()
    expected = 0
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

# Dependencies:
#   insert_head()
def test_str():

    # Empty
    list = DoublyLL(); test = Solution()
    expected = str(test)
    observed = str(list)
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # One
    list = DoublyLL(); test = Solution()
    list.insert_head(0); test.insert_head(0)
    expected = str(test)
    observed = str(list)
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"

    # Many
    list = DoublyLL(); test = Solution()
    for i in range(0, 30):
        list.insert_head(i)
        test.insert_head(i)
    expected = str(test)
    observed = str(list)
    assert(observed == expected), f"Observed: {observed} || Expected: {expected}"
    
# Dependencies:
#   every method
def test_all():
    l = DoublyLL()
    t = Solution()

    # Initial structure check
    assert str(l) == str(t), "Initialization mismatch."

    # Mixed insertion, removal, and search
    for i in range(50):
        l.insert_head(i)
        t.insert_head(i)
        if i % 10 == 0:
            l.remove(i // 2)
            t.remove(i // 2)
        l.insert_tail(i + 50)
        t.insert_tail(i + 50)

    # Mid-test structure check
    assert str(l) == str(t), "Mid-test structure mismatch."

    # Searching and removing
    for i in range(25, 75):
        if l.search(i) is not None:
            l.remove(i)
            t.remove(i)
        if l.search(i + 50) is not None:
            l.remove(i + 50)
            t.remove(i + 50)

    # Head and tail operations
    for _ in range(10):
        l.remove_head()
        t.remove_head()
        l.remove_tail()
        t.remove_tail()

    # Final removals to clear list
    while l.head:
        l.remove(l.head.data)
        t.remove(t.head.data)

    # Final structure check
    assert str(l) == str(t), "Final structure mismatch after all operations."




