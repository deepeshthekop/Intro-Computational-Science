# Plotting and Visualizing a Nonlinear Function
#f(x) = x^2 + 3
#Plot the graph of this function using Python. Choose a suitable range of x values (for example, from -10 to 10).
#Observe the shape of the graph. 
#Identify the minimum point of the function by looking at the graph.

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100)
y = x**2 + 3

plt.plot(x, y)
plt.title("Graph of f(x) = x^2 + 3")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()