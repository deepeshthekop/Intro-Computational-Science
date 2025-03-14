# Plotting and Visualizing a Nonlinear Function
#f(x) = x^3 - 3*x^2
#Plot the graph of this function using Python. Choose a suitable range of x values
#Observe the shape of the graph. 
#Identify the minimum/maximum point of the function by looking at the graph.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-2, 4, 100)
y = x**3 - 3*(x**2)

plt.plot(x, y)
plt.title("Graph of f(x) = x^3 - 3*x^2")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()