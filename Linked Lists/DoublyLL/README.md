# Doubly LinkedList Project Guide

## Overview

If you haven't completed the LinkedList project, then I encourage you to. This project builds upon the foundational knowledge of LinkedLists, diving into the implementation of a Doubly LinkedList (DLL). Doubly LinkedLists enhance the basic LinkedList structure by allowing bidirectional traversal, thanks to each node being linked to both its predecessor and successor. This capability enhances the efficiency of certain operations, though it comes at the cost of increased memory usage due to the additional pointers.

### Why Doubly LinkedLists?

Doubly LinkedLists offer greater flexibility than their singly linked counterparts. The ability to traverse backwards from any given node makes operations like reverse traversal and deletion more efficient, as there's no need to iterate from the head to find a node's predecessor. This added efficiency is particularly beneficial in applications requiring frequent bidirectional navigation or modifications at both ends of the list. However, this efficiency comes with the trade-off of increased memory usage, a consideration that is especially important in memory-constrained environments or languages like C, where memory management is manual.

## Project Structure

The project consists of three primary files, each serving a specific purpose:

- `DLL.py`: The main file where your Doubly LinkedList implementation will reside. This file outlines the basic structure and methods your DLL should support. Complete the outlined methods, keeping efficiency and memory usage in mind.

- `DLLSolutions.py`: Contains reference implementations for the Doubly LinkedList methods. Use this file as a guide if you encounter difficulties, but try to solve the challenges independently before consulting these solutions.

- `Test_DLL.py`: A suite of tests designed to validate your Doubly LinkedList's functionality, with a focus on correctness, efficiency, and edge case handling. Given the emphasis on time and efficiency in some tests, consider your implementation strategies carefully.

### Running the Tests

Make sure pytest is installed to run the test suite. Follow these steps to set up your testing environment:

#### For Windows Users

1. Install pytest via pip if you haven't already:
    ```
    python -m pip install pytest
    ```

2. Execute the tests with:
    ```
    pytest Test_DLL.py
    ```

Alternatively, Visual Studio Code can leverage extensions supporting pytest for integrated testing.

### Implementation Notes

As your data structure grows in complexity, adopting a more defensive programming approach becomes crucial. The inclusion of a `prev` field in each node opens the door for more efficient algorithms but also introduces additional complexity in memory management and algorithm design. Balancing efficiency with resource usage is key, especially when considering applications in environments with strict memory constraints. However, since we are using python, we don't have to worry about memory TOO much.

### Disclaimer

Please only modify the `DLL.py` file. The other files such as `DLLSolutions.py` and `Test_DLL.py` are provided for reference and testing purposes only. Modifying them may impact your project's testing outcomes.

This project's purpose is to deepen your understanding of complex data structures and their trade-offs. Feedback and suggestions would be appreciated.
