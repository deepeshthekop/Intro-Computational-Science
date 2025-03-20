import math
import matplotlib.pyplot as plt
import numpy as np

#y = np.log(x) + np.sin(x)

x_vals = np.linspace(0.1, 6, 300)
y_vals = np.log(x_vals) + np.sin(x_vals)

plt.plot(x_vals, y_vals, label='f(x) = ln(x) + sin(x)')
plt.title('graph of f(x) = ln(x) + sin(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid()
plt.show()