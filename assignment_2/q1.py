from scipy.optimize import linprog

#define coefficients for objective function
c = [-250, -180]

#define constraints
A_ub = [[10, 6], [4, 4]]
b_ub = [600, 280]

#define bounds for decision variables
bounds = [(0, None), (0, None)]

#solve the linear optimization problem
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method = "highs")

#print the required results
print("Maximum Profit: $", round(-result.fun))
print("Laptops: ", round(result.x[0]))
print("Tablets: ", round(result.x[1]))