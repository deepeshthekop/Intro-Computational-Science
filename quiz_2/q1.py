import numpy as np
from scipy.optimize import linprog

# Coefficients of objective function
c = [-300, -250, -180]

# Coefficients of resource constraints
A = [[6, 5, 3], [3, 3, 2], [5, 4, 3]]
b = [540, 310, 470]

# Bounds
bounds = [(0, None), (0, None), (0, None)]

# Solving the problem
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Printing the results
print("Maximum Total Profit: $", -result.fun)
print("Optimal Production Quantities: ", result.x)
print("Printer: ", result.x[0])
print("Monitor: ", result.x[1])
print("Keyboard: ", result.x[2])