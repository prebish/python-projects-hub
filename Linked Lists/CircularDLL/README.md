# Circular Doubly LinkedList Project Guide

## Overview

This project is an advanced iteration of the Doubly LinkedList (DLL) structure, introducing the Circular Doubly LinkedList (CDLL). CDLLs expand on DLLs by having the head and tail nodes linked to each other, forming a circle. This circular nature allows for endless iteration over the list, enhancing the DLL's flexibility with more complex operations that require wrapping from the end to the beginning of the list and vice versa.

### Why Circular Doubly LinkedLists?

Circular Doubly LinkedLists inherit all the benefits of standard DLLs—such as bidirectional traversal and efficient insertions/deletions at both ends—while adding the ability to loop the list infinitely. This is particularly useful in applications requiring cyclic data access patterns, like round-robin scheduling, music playlists, or implementing undo functionality in software. The trade-off for these capabilities is the need for more careful management to avoid infinite loops and ensure correct insertion and deletion at the boundaries of the list.

## Project Structure

The project includes three main files, tailored to guide the implementation and testing of your Circular Doubly LinkedList:

- `CDLL.py`: Your primary implementation file for the Circular Doubly LinkedList. This file outlines the skeleton of your CDLL, including the necessary methods and attributes. Focus on leveraging the circular and bidirectional nature of the structure to optimize the performance of each method.

- `CDLLSolutions.py`: Provides reference implementations for the Circular Doubly LinkedList methods. While available for consultation, challenge yourself to work through the problems independently before looking at these solutions.

- `Test_CDLL.py`: A comprehensive test suite designed to validate the functionality of your CDLL. It tests for correctness, efficiency, and edge cases. The circular aspect of the list means that some tests will specifically check for proper management of the looping nature of the structure.

### Running the Tests

Ensure pytest is installed to run the provided test suite efficiently. Follow these setup instructions:

#### For Windows Users

1. Install pytest using pip, if not already installed:
    ```
    python -m pip install pytest
    ```

2. To execute the tests, run:
    ```
    pytest Test_CDLL.py
    ```

Visual Studio Code users can use extensions that support pytest for an integrated testing experience.

### Implementation Notes

The Circular Doubly LinkedList's unique structure demands a defensive programming style to manage the additional complexity effectively. The seamless navigation from tail to head (and vice versa) introduces new challenges in maintaining the integrity of the list, especially when adding or removing nodes. As you implement your CDLL, consider not only the efficiency of operations but also the robustness of your structure in handling edge cases and ensuring the list remains well-formed under all conditions.

### Disclaimer

Your modifications should be confined to the `CDLL.py` file. The `CDLLSolutions.py` and `Test_CDLL.py` files are provided to aid your development and testing process; altering them could affect the outcomes of your project tests.
