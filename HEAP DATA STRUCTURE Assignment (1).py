#!/usr/bin/env python
# coding: utf-8
1. Describe Python's built-in data structure?
2. Describe the Python user data structure?
3. Describe the stages involved in writing an algorithm?
4. Outline the components of a good algorithm?
5. Describe the Tree traversal method?

6. Explain the difference between inorder and postorder tree traversal?Q. 1. Describe Python's built-in data structure?
Sol:
Python has four basic inbuilt data structures namely Lists, Dictionary, Tuple and Set.
These almost cover 80% of the our real world data structures. This  will cover the
above mentioned topics.

1. List

A list is a data structure that holds an ordered collection of items i.e. you can store a sequence of items in a list.

Python list is mutable which means it can be modified after its creation.

The items of lists are enclosed within the square bracket [] and separated by the comma.

2. Tuple

Python Tuple is used to store the sequence of immutable Python objects.

The tuple is similar to lists but it is different in the way that the value of the items stored in the list can be changed, whereas the tuple is immutable i.e. the value of the items stored in the tuple cannot be changed.

3. Dictionary

A dictionary is an unordered collection of data values used to store data values like a map.

Unlike other data types that hold only a single value as an element, Dictionary holds a key value pair.

4. Sets

A set is a collection that is unordered and unindexed.

Sets are written with curly brackets in Python.

Sets do not contain repetitive elements i.e. duplication of elements is removed from the sets.Q. 2. Describe the Python user data structure?
Sol:User-defined data structures: Data structures that aren’t supported by python but
can be programmed to reflect the same functionality using concepts supported by python
are user-defined data structures. There are many data structure that can be implemented
this way like Stack, Queue, Tree, Linked List, Graph, and Hash Map.

Stack

Stacks are linear Data Structures which are based on the principle of Last-In-First-Out (LIFO) where data which is entered last will be the first to get accessed.

Queue

A queue is also a linear data structure which is based on the principle of First-In-First-Out (FIFO) where the data entered first will be accessed first.

Linked List

Linked lists are linear Data Structures which are not stored consequently but are linked with each other using pointers. The node of a linked list is composed of data and a pointer called next.

Tree

A tree is a non-linear data structure consisting of roots and nodes. The topmost base node is the root, and the elements present at the end of the tree are leaves. 

Graph

A graph is a non-linear data structure consisting of nodes and edges. Nodes are known as vertices, and the lines connecting two nodes are generally called nodes.

HashMap

Hash Maps are indexed data structures and perform the same function as that performed by dictionary in Python. A hash map uses a hash function to compute index-key values into arrays. 

Q. 3. Describe the stages involved in writing an algorithm?
Sol : AEvery algorithm needs a process in order to be created and utilized. Described below are the four
stages of algorithm analysis and design:
1. Design

        The first stage is to identify the problem and thoroughly understand it. This is where it’s important
you consult with everybody who has an interest in the problem. Speak with them and see how they
see the problem and what they need out of the solution so their part of the project or program can
progress.

After you obtain the input, break out the problem into stages and calculate what happens at each
step so the next step can occur. All of this is elementary and you probably did this from the first
computer science class you ever took, but the same basic rules apply.
This is also the point where you are going to flowchart and/or use pseudo code to work out the
specific problems of solving the flow of operations within the code.

2.  Analyze

          Once you have the basic framework of the algorithm it’s time to start analyzing how efficient the
code is in solving the problem. Algorithm design is fluid and subject to individual plans. This is a
step that some programmers like to attack after they have coded the algorithm and run it through
the compiler. Others prefer to examine it prior to writing the code and analyze results based on
their expectations from the design stage.
Either way, what you are doing is looking for the efficiency of the algorithm. Algorithms are
measured in time and space for their efficiency. Look at the algorithm you’re designing and see
how it works with different size data structures and what kind of time it takes to work through
those structures. The problem here is deciding when the algorithm has reached maximum
efficiency for the project and produces acceptable results.

3. Implement:_
            Writing and coding the algorithm is the next step in the process. If you are the one writing the
algorithm, then you need to write it in the coding language you understand the best. In order for
you to know how to write the algorithm efficiently you have to know exactly what each line of
code is going to accomplish when the program is executed. Write the code to execute quickly but
can also handle the input data that it will receive.
If you are part of a team then have the best programmer in your group write the initial code, notate
it well so the lesser experienced programmers will understand what is happening as the application
is executed.

4. Experiment:

          Once the algorithm is designed and coded go back and experiment with different variables in the
algorithm. Try and enter data that will make it fail or try and re-write the code to work it out most
efficiently. Experimentation in algorithmic design is really just another step of the analyzing of the
algorithm. Keep attacking the efficiency aspect until it executes as much data as necessary in the
smallest amount of time. When you find flaws in what you have written or ways to write the code
better, then go back to the design step and redesign the algorithm.
The design and analysis of algorithms is a circular process. You may find yourself becoming
involved in any one of the steps. An experiment on an existing algorithm might lead to a new
design. Or a re-coding of an algorithm might lead to a more efficient execution. Wherever you find
yourself, keep working towards the goal of efficiency of the algorithm.Q. 4. Outline the components of a good algorithm?

Sol: Below are the main components of a good algorithm
    
1. Unambiguous − Algorithm should be clear.
2. Input − An algorithm should have 0 or more well-defined inputs.
3. Output − An algorithm should have 1 or more well-defined outputs, and should match the desired output.
4. Finiteness − Algorithms must terminate after a finite number of steps.
5. Well-Ordered - The exact order of operations performed in an algorithm should be concretely defined.
6. Independent - An algorithm should have step-by-step directions, which should be independent of any programming code.Q. 5. Describe the Tree traversal method?
Sol: Tree traversal involves traversing each node of the tree at least once where the information in the form of key and value can be retrieved for easy identification.

The following are the three different ways of traversal:

Inorder traversal

An inorder traversal is a traversal technique that follows the policy, i.e., Left Root Right.

Here, the left subtree of the root node is traversed first, then the root node, and then the right subtree of the root node is traversed.

Preorder traversal

A preorder traversal is a traversal technique that follows the policy, i.e., Root Left Right.

In this method it is the root node which is visited first and then the left sub-tree is traversed and finally at the end the right sub-tree.

Postorder traversal

A Postorder traversal is a traversal technique that follows the policy, i.e., Left Right Root.

In this method it is the left side is visited first and then the right-side sub-tree is traversed and finally at the node.

Q. 6. Explain the difference between inorder and postorder tree traversal?

Sol :INORDER TRAVERSAL -

An inorder traversal is a traversal technique that follows the policy, i.e., Left -> Root -> Right.

Here, the left subtree of the root node is traversed first, then the root node, and then the right subtree of the root node is traversed.

POSTORDER TRAVERSAL -

A Postorder traversal is a traversal technique that follows the policy, i.e., Left -> Right -> Root.

Here, the left subtree of the root node is traversed first, then the right-side sub-tree, and then finally the node is traversed.