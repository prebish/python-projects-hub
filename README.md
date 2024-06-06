# Programming Projects Hub

### Author: Joel Prebish  
### Date: 04/01/2024

## Overview

Welcome to the Programming Projects Hub, a comprehensive collection of projects designed to refine your programming skills through practical application. This repository is structured to cater to programmers of all levels, from beginners to advanced developers, providing a hands-on approach to mastering various programming concepts.

### Table of Contents

- [Overview](#overview)
- [Getting Started](#getting-started)
- [Testing with Pytest](#testing-with-pytest)
- [Conclusion](#conclusion)
- [Project Directory](#project-directory)
- [Disclaimer](#disclaimer)

## Getting Started

Each project comes with its own set of requirements and starter files to guide you through the completion process. Begin by reviewing the `README.md` file in each project directory for an overview and specific instructions.

To install the necessary dependencies for a project, navigate to its directory and run the appropriate command for your operating system:

- Windows: `pip install -r requirements.txt` or `python -m pip install -r requirements.txt`
- MacOS/Linux: `pip3 install -r requirements.txt`

### Repository Contents

Within this hub, you'll find individual folders for each project. Every folder contains:
- A `README.md` file with specifics about the project, its goals, and learning outcomes.
- Starter files (`*.py`) to jumpstart the project.
- A solutions file (`*Solutions.py`) with detailed example implementations.
- A tests file (`Test_*.py`) containing Pytest test suite(s) to ensure functionality and encourage test-driven development (TDD).

## Testing with Pytest

In this repository, we prioritize the Test-Driven Development (TDD) approach to enhance the quality and reliability of code. Each project is accompanied by a `Test_*.py` file, which contains a comprehensive suite of tests built with Pytest. These tests are designed to validate that your code meets the specified functionality requirements.

### Setting Up Pytest

To run the tests, you will need to install Pytest, a powerful and flexible testing tool in Python. Here’s how you can install it:

- Open your terminal or command prompt.
- Run the following command to install Pytest: `pip install pytest`

### Running Tests in VS Code

While you can write and execute your code in Visual Studio Code (VS Code), detailed test results and debugging are often clearer when viewed in the command line interface. However, for convenience, you can also run Pytest directly within VS Code using its integrated terminal.

### Getting Detailed Test Output

For a more comprehensive view of what each test is doing and to get detailed output in case of failures or errors, it's recommended to run the tests from the command line. Navigate to the project directory and run: `pytest Test_*.py`

This command will execute the test suite and provide detailed information on the tests passed, failed, and any errors encountered, along with the reasons for any failures. This detailed feedback is invaluable for debugging and improving your code.

Remember, the goal of TDD and these tests is not just to get your code to work, but to ensure it works correctly under various conditions and changes. Happy coding and testing!

## Conclusion

Whether you're taking your first steps in programming or seeking to master advanced concepts, the Programming Projects Hub offers a pathway to enhance your coding skills and deepen your understanding of software development.

## Project Directory

Projects are categorized by topic and arranged in increasing order of complexity. Some projects are standalone, while others build upon previous ones, allowing for progressive learning.

1. **Basic Memory**
    - [Stacks](./Basic%20Memory/Stacks/README.md)
    - Queues _(Coming Soon)_
2. **File Handling**
    - Reading/Writing **(TBD)**
    - Simple Encryption **(TBD)**
    - Simple Decryption **(TBD)**
3. **Sets and Operations**
    - Operations **(TBD)**
    - Set Abstract Data Type (ADT) **(TBD)**
    - Card Game (War) **(TBD)**
4. **Linked Lists**
    - [Linked List (LL)](./Linked%20Lists/LinkedList/README.md)
    - [Doubly LL (DLL)](./Linked%20Lists/DoublyLL/README.md)
    - [Circular DLL (CDLL)](./Linked%20Lists/CircularDLL/README.md)
5. **Bitmaps**
    - Reading **(TBD)**
    - BMP Editor **(TBD)**
6. **Hashing**
    - Hash Function **(TBD)**
    - HashSet **(TBD)**
7. **Search Trees**
    - Binary Search Tree (BST) **(TBD)**
    - Tree Set **(TBD)**
    - Red-Black BST **(TBD)**
8. **Tries (ReTRIEval Trees)**
    - The Simple Trie (Prefix Tree) **(TBD)**
    - De La Briandais Trie (DLB) **(TBD)**
9. **Compression Algs**
    - Run Length Encoding (RLE) **(TBD)**
    - Lempel Ziv-Welch (LZW) **(TBD)**
10. **Graphing**
    - 2D Array Based **(TBD)**
    - Adjacency Based **(TBD)**
11. **More Memory**
    - System Quirks **(TBD)**
    - Memory **(TBD)**

### Disclaimer

Focus on understanding and completing the projects as outlined. The structure of each project is designed to guide your learning experience. While modifications and experimentation within the project scope are encouraged, it's crucial to only alter files explicitly designated for changes. Modifying other files or the project structure could disrupt the intended learning path and functionality. Adhere to the instructions in each project's `README.md` to ensure a comprehensive and effective learning experience.

