import matplotlib.pyplot as plt
import numpy as np

#define range
x1 = np.linspace(0, 100, 200)

#defining constraints
x2_assembly = (600 - 10*x1) / 6
x2_testing = (280 - 4*x1) / 4

#plot constraints
plt.plot(x1, x2_assembly, label='10*x1 + 6*x2 <= 600')
plt.plot(x1, x2_testing, label='4*x1 + 4*x2 <= 280')

#plot feasible region
plt.fill_between(x1, np.minimum(x2_assembly, x2_testing), 0, color='gray')

#identify corner points of the feasible region
corner_points = [(0, 0), (60, 0), (0, 70), (45, 25)]
for point in corner_points:
    plt.scatter(*point, color='red')
    plt.text(point[0], point[1], f'({point[0]}, {point[1]})', fontsize=10, verticalalignment='bottom')

#plot and labels
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.xlabel('Laptops (x1)')
plt.ylabel('Tablets (x2)')
plt.title("Graphical Representation of Linear Optimization")
plt.legend()
plt.grid()
plt.show()