import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt

x = np.arange(0, np.pi, 0.01)
f = np.sin(x)

F_exact = -np.cos(x)

F_approx = cumulative_trapezoid(f, x, initial=0)

plt.figure(figsize=(10, 6), constrained_layout=True)
plt.plot(x, F_exact, label='Exact Integral')
plt.plot(x, F_approx, label='Approximate Integral using Trapezoid Rule', linestyle='--')
plt.grid()
plt.title('Comparison of Exact vs Approximate Integral', fontsize=14)
plt.xlabel('x')
plt.ylabel('F(x)')
plt.legend()
plt.show()