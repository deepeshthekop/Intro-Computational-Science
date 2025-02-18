import numpy as np

a = 0
b = np.pi
n = 11

h = (b-a)/(n-1)

x = np.linspace(a, b, n)
f = np.sin(x)

I_trap = h/2 * (f[0] + 2*np.sum(f[1:n-1]) + f[n-1])
Error_trap = 2 - I_trap

print("I_trap = ", I_trap)
print("Error in I_trap = ", Error_trap)