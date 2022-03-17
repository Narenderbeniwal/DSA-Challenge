#!/usr/bin/env python
# coding: utf-8
1. What is the divide and conquer strategy?
2. What is binary search and how does it work?
3. Explain the distinction between a list and a tuple.
4. Can you explain how Python manages memory?
5. What is the difference between pickling and unpickling?
6. What are the different types of search algorithms?Q. 1. What is the divide and conquer strategy?
Sol:

In divide and conquer approach, the problem in hand, is divided into smaller sub-problems and then each problem is solved independently. When we keep on dividing the subproblems into even smaller sub-problems, we may eventually reach a stage where no more division is possible. Those "atomic" smallest possible sub-problem (fractions) are solved. The solution of all sub-problems is finally merged in order to obtain the solution of an original problem.

Broadly, we can understand divide-and-conquer approach in a three-step process.

Divide/Break
This step involves breaking the problem into smaller sub-problems. Sub-problems should represent a part of the original problem. This step generally takes a recursive approach to divide the problem until no sub-problem is further divisible. At this stage, sub-problems become atomic in nature but still represent some part of the actual problem.

Conquer/Solve
This step receives a lot of smaller sub-problems to be solved. Generally, at this level, the problems are considered 'solved' on their own.

Merge/Combine
When the smaller sub-problems are solved, this stage recursively combines them until they formulate a solution of the original problem. This algorithmic approach works recursively and conquer & merge steps works so close that they appear as one.


    Q. 2. What is binary search and how does it work?
Sol: 
    Binary search is an efficient algorithm for finding an item from a sorted list of items. 
It works by repeatedly dividing in half the portion of the list that could contain the item, 
until you've narrowed down the possible locations to just one.
suppose we have a list of sorted elements, this algorithm first divide this list from middle then
it searchs that the element is less than this middle elemnt or greater than this element. then in
the basis of that it diveds again by the middle.
Q. 3. Explain the distinction between a list and a tuple.
Sol:
1.	List is mutable.	Tuples are immutable
2.	List iteration is slower and time-consuming.	Tuples iteration is faster.
3.	List is performed well in insertion and deletion operations.	Tuples are performed well in accessing elements operations.
4.	List takes more memory	Tuples take less memory.
5.	Lists are many built-in methods	Tuples are less in-built methods.
6.	In List Error is more likely to happen.	In Tuples Error hardly takes place.
7. 	Lists can be used to store homogeneous and heterogeneous elements.	Tuples are used to store only heterogeneous elements.Q. 4. Can you explain how Python manages memory?
Sol: 
    Memory management in python is managed by Python private heap space. All Python objects and data structures are located in a private heap. The programmer does not have access to this private heap. The python interpreter takes care of this instead.

The allocation of heap space for Python objects is done by Python’s memory manager.

Python also has an inbuilt garbage collector, which recycles all the unused memory and so that it can be made available to the heap space.

Q. 5. What is the difference between pickling and unpickling?
Sol :“Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, 
and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like
object) is converted back into an object hierarchy.Q. 6. What are the different types of search algorithms?
Sol :
  Different types of search algorithms  are as below:
Linear Search.
Binary Search.
Jump Search.
Interpolation Search.
Exponential Search.
Sublist Search (Search a linked list in another list)
Fibonacci Search.

# In[ ]:




