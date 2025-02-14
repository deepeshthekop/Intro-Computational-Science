import numpy as np

a = 0
b = np.pi
n = 11

h = (b-a)/(n-1)

x = np.linspace(a, b, n)
f = np.sin(x)

I_simp = (h/3) * (f[0] + 4*np.sum(f[1:n-1:2]) + 2*np.sum(f[:n-2:2]) + f[n-1])
Error_simp = 2 - I_simp

print("I_simp = ", I_simp)
print("Error in S_trap = ", Error_simp)