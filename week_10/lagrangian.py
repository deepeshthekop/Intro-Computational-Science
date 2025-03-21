#lagrangain method of linear system of equations

import numpy as np

# coefficient matrix A
A = np.array([[2,2,1,1], [2,6,1,-1], [1,1,0,0], [1,-1,0,0]])

# right-hand side vector b
b = np.array([0,0,4,2])

# solve the system of equations
solution = np.linalg.solve(A, b)

print("x =", solution[0])
print("y =", solution[1])
print("lambda1 =", solution[2])
print("lambda2 =", solution[3])