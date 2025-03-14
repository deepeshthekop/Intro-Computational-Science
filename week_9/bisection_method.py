import numpy as np

a = 0
b = 1

tolerance = 0.001

f_a = np.cos(a) - a
f_b = np.cos(b) - b 

while (b - a) / 2 > tolerance:
    x_mid = (a + b) / 2
    f_mid = np.cos(x_mid) - x_mid

    if f_mid == 0:
        break

    elif f_a * f_mid < 0:
        b = x_mid
        f_b = f_mid
    
    else:
        a = x_mid
        f_a = f_mid


approx_root = (a + b) / 2

print("Approximate root using Bisection Method = ", approx_root)