# function is f(x) = cos(x); whose derivative is -sin(x)

import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('seaborn-poster')

h = 0.1 # step size
x = np.arange(0, 2*np.pi, h) # define grid
y = np.cos(x) # compute function

backward_difference = np.diff(y)/h # compute vector of backward differences
x_diff = x[1:] # compute corresponding grid
exact_solution = -np.sin(x_diff) # compute exact solution

#plot solution
plt.figure(figsize=(12, 8))
plt.plot(x_diff, backward_difference, "-", label='Finite Difference Approximation')
plt.plot(x_diff, exact_solution, label='Exact Solution')
plt.legend()
plt.show()

#compute max error between exact solution and numerical derivate
max_error = max(abs(exact_solution - backward_difference))
print(max_error)