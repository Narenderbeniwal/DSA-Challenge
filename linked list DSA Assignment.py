#!/usr/bin/env python
# coding: utf-8
1. What is a linked list?

2. What are the different forms of linked lists?

3. What is a linked list's purpose?
4. What are the advantages of linked lists over arrays?
5. What is the purpose of a circular linked list?
6. How will you explain Circular Linked List?Q. 1 What is a linked list?
Sol: 
    A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations. The elements in a linked list are linked using pointers.
    
    Each node of a list is made up of two items - the data and a reference to the next node. The last node has a reference to null. The entry point into a linked list is called the head of the list.

Linked lists are typically used to create file systems, adjacency lists, ​and hash tables.

Q. 2. What are the different forms of linked lists?
Sol: There are four key types of linked lists:

1. Singly Linked List

The singly linked list is a data structure that contains two parts, i.e., one is the data part, and the other one is the address part, which contains the address of the next or the successor node. The address part in a node is also known as a pointer. Here, we can only traverse in one direction only, reverse is not possible.


2. Doubly linked list:

A doubly linked list is a list that has three parts in a single node, includes one data part, a pointer to its previous node, and a pointer to the next node. Or we can say that we can traverse in both the direction as every node contains an additional prev pointer that points to the previous node.

3. Circular linked list:

The circular linked list is a list in which the last node connects to the first node, so the link part of the last node holds the first node's address. The circular linked list has no starting and ending node. Or, here we can keep traversing forever and ever until the program crashes as the tail node's next pointer points to the head node instead of a NULL.

4. Doubly Circular linked List:

Here, the last node is attached to the first node and thus creates a circle. It is a doubly linked list also because each node holds the address of the previous node also.

It is a two-way circular linked list which is a more complex kind of Linked List containing a pointer to the succeeding as well as the preceding node in the series.


Q. 3. What is a linked list's purpose?

Sol:
    1. Linked Lists are often used because of their efficient insertion and deletion operations. Since Every node in linked list contains a data and address part, hence it becomes easy to locate the element or node's data with help of its address.

2. To prevent the collision between the data in the hash map, we use a singly linked list.

3. Also, to solve and store the values of polynomial algebra, it is sometimes difficult to deal with large integers, hence in this case, we use linked list data structures.
Q. 4. What are the advantages of linked lists over arrays?

Sol: Arrays are bound by the limitation of their size as we have to specify the number of elements in the array beforehand. Whereas in the linked list we can add any number of elements.

Linked list provide an efficient way of storing related data and perform basic operations such as insertion, deletion and updating of information at the cost of extra space required for storing the address.

There is no need to specify how many number of nodes required so linked list does not waste memory space. We can allocate and de-allocate memory space at runtime.

Q. 5. What is the purpose of a circular linked list?
S:
    A Circular list is a linked list where the last node in the linked list points to the first node in the list. A Circular list does not contain NULL pointers.

Circular linked lists are widely used in applications where tasks are to be repeated or in time sharing applications.

There are several applications where circular list can be used :

1. In Implementation of round-robin scheduling in system processes

2. In Implementation of circular scheduling in high-speed graphics

3. A good example of an application where circular linked list should be used is a timesharing problem solved by the operating system.

4. It is used in multiplayer games to give a chance to each player to play the game. where we can easily shuffle back to the first player from the last player quickly, utilizing the circular property.

Q.6. How will you explain Circular Linked List?

Sol:
    A circular linked is very similar to a singly linked list, the only difference is in the singly linked list the last node of the list point to null but in the circular linked list the last node of the list point to the address of the head. This type of list is known as a circular linked list.
    
    The circular linked list has no beginning and no ending and there is no null value present in the next part of any of the nodes.

The circular linked list has a dynamic size which means the memory can be allocated when it is required.




# In[ ]:




