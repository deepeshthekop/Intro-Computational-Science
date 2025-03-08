import matplotlib.pyplot as plt
import numpy as np

x1 = np.linspace(0, 100, 200)

x2_1 = (200 - 4*x1) / 2
x2_2 = (300 - 10*x1) / 5

plt.plot(x1, x2_1, label='4x1 + 2x2 <= 200 (Labor)')
plt.plot(x1, x2_2, label='10x1 + 5x2 <= 300 (Wood)')

plt.fill_between(x1, np.minimum(x2_1, x2_2), 0, color='gray')

plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel('Tables (x1)')
plt.ylabel('Chairs (x2)')
plt.title("Graphical Representation of Linear Optimization")
plt.legend()
plt.grid()
plt.show()