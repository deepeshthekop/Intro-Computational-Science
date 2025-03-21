#lagrangain method of non-linear system of equations

from scipy.optimize import fsolve

def equations(vars):
    x, y, lambda1 = vars

    eq1 = 3*x**2 + lambda1
    eq2 = 2*y + lambda1
    eq3 = x + y - 4

    return [eq1, eq2, eq3]

# initial guess
initial_guess = [1, 1, 1]

# solve the system of equations
solution = fsolve(equations, initial_guess)

print("x =", solution[0])
print("y =", solution[1])
print("lambda1 =", solution[2])

min_value = solution[0]**3 + solution[1]**2
print("Minimum value of f(x, y) = x^3 + y^2 =", min_value)