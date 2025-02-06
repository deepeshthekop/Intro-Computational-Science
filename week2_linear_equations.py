import numpy as np

A = np.array([[4, 3, -5], [-2, -4, 5], [8, 8, 0]])

y = np.array([2, 5, -3])

x = np.linalg.solve(A, y)

print("\n")

print("Solution vector x: ", x)

print("\n")