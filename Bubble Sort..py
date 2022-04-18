#!/usr/bin/env python
# coding: utf-8

# # RIZWAN AHMAD

# Q.program to implement Early Termination Bubble Sort. Show Each Iteration of the bubble sort.

# In[3]:


# program to implement Early Termination Bubble Sort. Show Each Iteration of the bubble sort
lst=[9,79,49,59]
print("Unsorted list :", lst)
print()

for j in range(len(lst)-1):
    for i in range(len(lst)-1):
        if lst[i]>lst[i+1]:
            lst[i],lst[i+1]= lst[i+1],lst[i]
            print(lst)
        else:
            print(lst)
        print()

print("Sorted list :", lst)
print()


# In[ ]:




