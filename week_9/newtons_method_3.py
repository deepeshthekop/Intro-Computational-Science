import math

x = 2
tolerance = 0.001
max_iterations = 2

for i in range(max_iterations):
    fx = math.log(x) + math.sin(x)
    f_prime = 1/x + math.cos(x)
    f_double_prime = -1/x**2 - math.sin(x)

    if f_double_prime == 0:
        print("second derivative is 0, cannot continue")
        break

    elif abs(f_prime) < tolerance:
        print("critical point found, f'(x) is very small, good result")
        break

    else:
        x = x - f_prime / f_double_prime

print("final result, minimun or maximum occurs at x ~ ", x)