#!/usr/bin/env python
# coding: utf-8

# # RIZWAN AHAMD

# Q.Write a program(in C/C++/Python) to implement the sparse Matrix. Take input matrix of size 'm' x 'n' and convert it into sparse matrix.

# In[1]:


import numpy as np
from scipy import sparse

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))
matrix = []
print("Enter the entries row wise:")
for i in range(R):          # row element entries
    a =[]
    for j in range(C):      # column element entries
        a.append(int(input()))
    matrix.append(a)

# For printing the matrix
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

print("The input matrix is:")
print(matrix)
sparse_matrix = sparse.csr_matrix(matrix)
print("The sparse matrix is:")
print(sparse_matrix)


# In[ ]:




