#f(x) = x.ln(x) + e^-x

import math

x = 1.5
tolerance = 0.001
max_iterations = 3

# Newton's method to find the minimum of the function
for i in range(max_iterations):
    fx = x*math.log(x) + math.exp(-x)
    f_prime = math.log(x) + 1 - math.exp(-x)
    f_double_prime = 1/x + math.exp(-x)

    if f_double_prime == 0:
        print("second derivative is 0. Cannot continue. Exiting...")
        break

    elif abs(f_prime) < tolerance:
        print("Critical point found. F'(x) is very small. Good result. Exiting...")
        break

    else:
        x = x - f_prime / f_double_prime
        print(f"Iteration {i}: x = ", x)

print("Minimun of the nonlinear function occurs at x ~ ", x)