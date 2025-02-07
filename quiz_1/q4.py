#QUESTION 4

import numpy as np

A = np.array([[2,-1,3],[1,4,5],[3,6,2]])

b = [1,2,3]

determinant = np.linalg.det(A)
print("Determinant of A: ", determinant)

dot_product = np.dot(A, b)
print("Dot product of A and vector b: ", dot_product)

transpose = np.transpose(A)
print("Transpose of A: ", transpose)