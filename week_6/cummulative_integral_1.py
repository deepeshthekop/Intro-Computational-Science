import numpy as np 

x = np.linspace(0, np.pi, 11)
f = np.sin(x)

I_trapz = np.trapezoid(f, x)
print(I_trapz)