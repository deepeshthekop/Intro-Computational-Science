#QUESTION 3

#f(x) = (x)^3*(e)^-x

import numpy as np
import math
import matplotlib.pyplot as plt

h = 0.1
x = np.arange(0, 3, h)
y = (pow(x,3))*(np.exp(-x))

forward_difference = np.diff(y)/h 
x_diff = x[:-1:]
exact_derivative = (3*pow(x[:-1],2)*np.exp(-x[:-1])) - (pow(x[:-1],3)*np.exp(-x[:-1]))

plt.figure(figsize=(12, 8))
plt.plot(x_diff, forward_difference, "--", label='Forward Difference Approximation')
plt.plot(x_diff, exact_derivative, label='Exact Derivative')
plt.legend()
plt.show()