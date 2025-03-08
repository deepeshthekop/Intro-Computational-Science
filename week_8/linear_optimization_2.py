from scipy.optimize import linprog

c = [-80, -50]

A_ub = [[4, 2], [10, 5]]

b_ub = [200, 300]

bounds = [(0, None), (0, None)]

result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method = "highs")

#print(result)
print(-result.fun)
print(result.x)