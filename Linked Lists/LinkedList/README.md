# LinkedList Project Guide

## Overview

This project is designed to provide practical experience with data structures, focusing specifically on the implementation of a simple LinkedList. LinkedLists are fundamental data structures in computer science, used to store collections of elements in a sequential manner. Unlike arrays, LinkedLists store elements in nodes that are linked together, making insertions and deletions more efficient in scenarios where these operations are frequent.

### Why LinkedLists?

LinkedLists are valuable for their dynamic size and ability to insert or delete nodes without reallocating or reorganizing the entire data structure. This makes them ideal for applications where the size of the data set changes frequently or the memory allocation needs to be efficient (like in C).

## Project Structure

This project comprises three main files:

- `LL.py`: This is the core file where you'll implement your LinkedList. It includes the basic structure and methods you need to define (plus some tips). Your task is to complete the implementation following the guidelines provided.

- `LLSolutions.py`: Contains the solutions for the LinkedList methods. It's meant to serve as a reference. Please try to solve the problems on your own before consulting this file. If you're stuck or curious, feel free to ask questions!

- `Test_LL.py`: This file includes a test suite to run against your LinkedList implementation. It will help you identify issues and ensure that your data structure behaves as expected. Testing your code early and often can save you a lot of debugging time, so please take advantage of this suite that I spent hours of my precious life slaving away at lol.

### Running the Tests

To run the tests, you'll need to have pytest installed. Here's how you can set up your environment:

#### For Windows Users

1. Install pytest:
    ```
    python -m pip install pytest
    ```

2. Run the tests:
    ```
    pytest Test_LL.py
    ```

You can also run the tests using an extension in Visual Studio Code that supports pytest, making the testing process more integrated into your development environment.

### Disclaimer

Please focus your modifications solely on the `LL.py` file. The other files are provided as references and for testing purposes. Changing them could affect the outcome of the tests.
