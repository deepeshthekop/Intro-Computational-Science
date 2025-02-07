import numpy as np

a = 1
b = 3

n = 3
h = (b-a)/n

x_points = np.linspace(a,b,n+1)

x_left = x_points[:-1]
I_left = h*np.sum(x_left**2)

x_right = x_points[1:]
I_right = h*np.sum(x_right**2)

x_mid = (x_left + x_right)/2
I_mid = h*np.sum(x_mid**2)

print("Left Riemann Sum=: ", I_left)
print("Right Riemann Sum: ", I_right)
print("Mid-point Riemann Sum: ", I_mid)