import numpy as np

A = np.array([[3, 2, -1], 
              [2, -3, 4], 
              [1, 1, 2]])

y = np.array([4, 5, 7])

solution = np.linalg.solve(A, y)

print("\n")

print(f"x = {solution[0]}, y = {solution[1]}, z = {solution[2]}" )

print("\n")