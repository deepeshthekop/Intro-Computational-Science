import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 * np.exp(-x) + np.sin(2 * x)

def exact_derivative(x):
    return (2 * x * np.exp(-x) - x**2 * np.exp(-x)) + 2 * np.cos(2 * x)

x_values = np.arange(0, 2.1, 0.1)
h = 0.1

print("Function values: ", f(x_values))

numerical_derivative = (f(x_values + h) - f(x_values - h)) / (2 * h)

exact_derivative_values = exact_derivative(x_values)

plt.plot(x_values, numerical_derivative, label='Numerical Derivative', linestyle='--')
plt.plot(x_values, exact_derivative_values, label='Exact Derivative')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Comparison of Numerical and Exact Derivative')
plt.legend()
plt.grid(True)
plt.show()