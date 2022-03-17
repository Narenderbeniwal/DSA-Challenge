#!/usr/bin/env python
# coding: utf-8
1. Use examples to explain the sorting algorithms.
2. What Are the Benefits of Stacks?

3. What is the difference between a stack and a queue?
4. What are the different forms of queues?
5. Why should I use Stack or Queue data structures instead of Arrays or
Lists, and when should I use them?
6. What is the significance of Stack being a recursive data structure?Q. 1. Use examples to explain the sorting algorithms.

Sol:
Sorting Algorithms are methods of reorganizing a large number of items into some specific order such as highest to lowest, or vice-versa, or even in some alphabetical order.

These algorithms take an input list, processes it (i.e, performs some operations on it) and produce the sorted list.

The most common example we experience every day is sorting clothes or other items on an e-commerce website either by lowest-price to highest, or list by popularity, or some other order.

Below are the few sorting algorithm available--
Selection Sort.
Bubble Sort.
Insertion Sort.
Merge Sort. etc.



Q. 2. What Are the Benefits of Stacks?
Sol:
    A Stack is a simple data structure for storing data.

In stack, the order in which the data arrives is important. Stacks are ideal for enforcing sequential rules of access ie, LIFO.

A Bunch of plates are the siples examples of stack.

Stacks are used for reversing things. If you push something, say a String onto a Stack one character at a time, and then construct a String from the members popped off the Stack, then the String is reversed.

ADVANTAGES

Easy to started
Less Hardware Requirement
Cross- PlatformQ. 3. What is the difference between a stack and a queue?

Sol :
Stack and Queue both are the non-primitive data structures. The main differences between stack 
and queue are that stack uses LIFO (last in first out) method to access and add data elements
whereas Queue uses FIFO (First in first out) method to access and add data elements.

Stack A stack is a linear data structure in which elements can be inserted and deleted only from one side of the list, called the top. A stack follows the LIFO (Last In First Out) principle, i.e., the element inserted at the last is the first element to come out. The insertion of an element into stack is called push operation, and deletion of an element from the stack is called pop operation. In stack we always keep track of the last element present in the list with a pointer called top.

Queue: A queue is a linear data structure in which elements can be inserted only from one side of the list called rear, and the elements can be deleted only from the other side called the front. The queue data structure follows the FIFO (First In First Out) principle, i.e. the element inserted at first in the list, is the first element to be removed from the list. The insertion of an element in a queue is called an enqueue operation and the deletion of an element is called a dequeue operation. In queue we always maintain two pointers, one pointing to the element which was inserted at the first and still present in the list with the front pointer and the second pointer pointing to the element inserted at the last with the rear pointer.
# ![Screen%20Shot%202022-03-17%20at%208.10.40%20AM.png](attachment:Screen%20Shot%202022-03-17%20at%208.10.40%20AM.png)
Q. 4. What are the different forms of queues?
Sol :
There are four different types of queues:
Simple Queue.
Circular Queue.
Priority Queue.
Double Ended Queue
Q. 5. Why should I use Stack or Queue data structures instead of Arrays or
Lists, and when should I use them?

Sol:
    When you want to remove something from the beginning of an array or a List (ArrayList) it usually
takes O(n) time, but for a queue it takes O(1) time. That can make a huge difference if there are
a lot of elements.The stack is a dynamic data structure means that size of the stack can grow or
shrink at run time. In contrast, the size of the array is fixed, and it cannot be modified at run
time. 
Q. 6. What is the significance of Stack being a recursive data structure?
Sol:
    Stack is a LIFO data structure i.e. ( Last In First Out) and hence it is used to implement 
recursion.When a function calls itself recursively, a return address needs to be stored for each
activation of the function so that it can later be used to return from the function activation. 
Stack structures provide this capability automatically.
# In[ ]:




