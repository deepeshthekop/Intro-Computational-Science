import numpy as np

a = 0
b = np.pi

n = 11
h = (b-a)/(n-1)

x_points = np.linspace(a,b,n)
#f = np.sin(x)

x_left = x_points[:n-1]
I_left = h*np.sum(np.sin(x_left))
I_left_error = 2 - I_left

x_right = x_points[1:]
I_right = h*np.sum(np.sin(x_right))
I_right_error = 2 - I_right

x_mid = (x_left + x_right)/2
I_mid = h*np.sum(np.sin(x_mid))
I_mid_error = 2 - I_mid

print("Left Riemann Sum: ", I_left)
print("Left Riemann Sum Error: ", I_left_error)

print("Right Riemann Sum: ", I_right)
print("Right Riemann Sum Error: ", I_right_error)

print("Mid-point Riemann Sum: ", I_mid)
print("Mid-point Riemann Sum Error: ", I_mid_error)