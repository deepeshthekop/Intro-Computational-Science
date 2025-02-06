import numpy as np
#from sympy import Matrix, pretty_print

matrix1 = np.array([
[2, 3, 1],
[4, 7, 5],
[6, 2, 8]
])

matrix2 = np.array([
[1, 3, 1],
[4, 2, 5],
[6, 2, 3]
])

print("Matrix 1: \n", matrix1)
print("Matrix 2: \n", matrix2)
print('\n')

det_matrix1 = np.linalg.det(matrix1)
det_matrix2 = np.linalg.det(matrix2)

print("Determinant of Matrix 1: ", det_matrix1)
print('\n')
print("Determinant of Matrix 2: ",det_matrix2)
print('\n')

inv_matrix1 = np.linalg.inv(matrix1)
inv_matrix2 = np.linalg.inv(matrix2)

print("Inverse of Matrix 1: \n",inv_matrix1)
print('\n')
print("Inverse of Matrix 2: \n",inv_matrix2)
print('\n')

sum_matrix = np.add(matrix1, matrix2)

print("Sum of Matrices: \n",sum_matrix)
print('\n')