#!/usr/bin/env python
# coding: utf-8
1. What exactly is an application tree?
2. What is pre-order tree traversal and how does it work?
3. What is the problem with the Hanoi Tower?
4. Can you explain the distinction between linear and nonlinear data
structures?

5. What is the distinction between a list and an array?Q. 1. What exactly is an application tree?
Sol :
K-D Tree: A space partitioning tree used to organize points in K dimensional space. 
Trie : Used to implement dictionaries with prefix lookup. 
Suffix Tree : For quick pattern searching in a fixed text. 
Spanning Trees and shortest path trees are used in routers and bridges respectively in computer 
networks.
Q. 2. What is pre-order tree traversal and how does it work?
Sol :
    
    A preorder traversal is a traversal technique that follows the policy, i.e., Root Left Right.

In this method it is the root node which is visited first and then the left sub-tree is traversed and finally at the end the right sub-tree.

The algorithm for preorder traversal is -

Algorithm Preorder(tree)

Visit the root.
Traverse the left subtree, i.e., call Preorder(left-subtree)
Traverse the right subtree, i.e., call Preorder(right-subtree)
Q. 3. What is the problem with the Hanoi Tower?
Sol:
    Tower of Hanoi is a mathematical problem (puzzle) that consists of 3 poles and ‘n’ number of discs, each disc having different diameters.

The objective of this problem is to transfer all the ‘n’ discs from source pole to the destination pole in such a way that we get the same arrangement of discs as before. But this goal must be achieved by sticking to the rules, which are -

1.Only one disc can be moved at a time.
2. Only the top-most disc can be removed
3. The larger disc cannot be placed on top of the smaller disc.
Q. 4. Can you explain the distinction between linear and nonlinear data
structures?
Sol: In linear data structure, data elements are sequentially connected and each element is traversable
through a single run. In non-linear data structure, data elements are hierarchically connected and
are present at various levels.
Q. 5. What is the distinction between a list and an array?
Sol:
 1. List is an in-build data structure of python language hence no module is to be imported before using it. But array is not an in-build data structure, so, we need to import the “array” module before creating and using arrays.

2. A python list is faster than a python array as python array are based on a python list itself.
3. The list cannot handle the direct arithmetic operations whereas Arrays can directly handle arithmetic operations.
4. Array stores homogeneous data values, and the list can store heterogeneous data values.
# In[ ]:




