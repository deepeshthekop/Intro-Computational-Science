from scipy.optimize import linprog

c = [200, 220]

A_ub = [[-0.7, -0.6], [0.9, 0.8]]
b_ub = [-0.65, 0.85]

A_eq = [[1, 1]]
b_eq = [1]

bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method = "highs")

#print(result)
print(result.fun)
print(result.x)