import numpy as np
import matplotlib.pyplot as plt

f = lambda t, s: np.exp(-t)
h = 0.1
t = np.arange(0, 1+h, h)
s0 = -1

s = np.zeros(len(t))
s[0] = s0

for i in range(0, len(t)-1):
    s[i+1] = s[i] + h*f(t[i], s[i])

plt.figure(figsize=(12, 8))
plt.plot(t, s, 'bo--', label='Approximate')
plt.plot(t, -np.exp(-t), 'g', label='Exact')
plt.title('Approximate and Exact solution for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show() 