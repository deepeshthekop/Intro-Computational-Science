x = 4
tolerance = 0.001
max_iterations = 3

for i in range(max_iterations):
    fx = x**3 - 6*x**2 + 9*x + 1.5
    f_prime = 3*x**2 - 12*x + 9
    f_double_prime = 6*x - 12

    if f_double_prime == 0:
        print("second derivative is 0, cannot continue")
        break

    elif abs(f_prime) < tolerance:
        print("critical point found, f'(x) is very small, good result")
        break

    else:
        x = x - f_prime / f_double_prime

print("final result, minimun or maximum occurs at x ~ ", x)