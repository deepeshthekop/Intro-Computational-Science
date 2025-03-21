import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-1, 5, 200)
y = x**3 - 6*x**2 + 9*x
y_prime = 3*x**2 - 12*x + 9


critical_points = np.roots([3, -12, 9])
print(critical_points)
critical_values = critical_points**3 - 6*critical_points**2 + 9*critical_points
print(critical_values)


plt.plot(x, y)
plt.scatter(critical_points, critical_values, color='red')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^3 - 6x^2 + 9x with critical points')
plt.grid()
plt.show()