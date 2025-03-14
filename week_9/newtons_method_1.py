#f(x) = x^3 - 2*x^2 + 3
#f'(x) = 3*x^2 - 4*x

x = 1
tolerance = 0.001
max_iterations = 3

for i in range(max_iterations):
    fx = x**3 - 2*x**2 + 3
    f_prime = 3*x**2 - 4*x

    if f_prime == 0:
        print("derivative is 0, cannot continue")
        break

    elif abs(fx) < tolerance:
        print("stopping, f(x) is close to zero, good result")
        break

    else:
        x = x - fx / f_prime

print("final result, root is approx x ~ ", x)