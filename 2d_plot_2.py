import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100) # x = [-5, -4.9, -4.8, ..., 4.9, 5]
y = x**2

plt.plot(x, y, "g-.") # green, dashed line

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of y = x^2')

plt.show()