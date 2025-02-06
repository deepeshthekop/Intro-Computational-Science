# f(x) = (X)2
# omega = 20
# epsilon = 0.1
# Range: -2 x2, step 200.

import numpy as np
import matplotlib.pyplot as plt

omega = 20
epsilon = 0.1
h = 200
x = np.linspace(-2, 2, h)
y_true = x**2
y_with_noise = y_true + epsilon*np.cos(omega*x)
y_true_derivative = 2*x
y_with_noise_derivative = y_true_derivative - epsilon*omega*np.sin(omega*x)

plt.figure(figsize=(12, 4)) # 12 inches wide and 4 inches tall

plt.subplot(1, 2, 1) # 1 row, 2 columns, 1st subplot
plt.plot(x, y_with_noise, "r-")
plt.plot(x, y_true, "b-")
plt.title("Noisy vs True")

plt.subplot(1, 2, 2) # 1 row, 2 columns, 2nd subplot
plt.plot(x, y_with_noise_derivative, "r-")
plt.plot(x, y_true_derivative, "b-")
plt.title("Noisy Derivative vs True Derivate")

plt.tight_layout() # adjust subplots to fit into figure area
plt.show() # display the figure