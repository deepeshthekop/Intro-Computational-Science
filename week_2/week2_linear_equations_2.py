import numpy as np

A = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])

y = np.array([2, 5, -3])

A_inverse = np.linalg.inv(A)

x = np.dot(A_inverse, y)

print("\n")

print("Solution vector x using matrix inversion: ", x)

print("\n")