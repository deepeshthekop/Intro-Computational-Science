#f'(S(t)) = -S(t)
#exact solution S(t) = e^(-t)
#initial condition S(0) = 1

import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

F = lambda t, s: -s # s'(t) = -s(t)

t_eval = np.arange(0, 1, 0.01)

sol = solve_ivp(F, [0, 1], [1], t_eval=t_eval)

plt.figure(figsize=(12, 4))
plt.subplot(121)
plt.plot(sol.t, sol.y[0])
plt.xlabel('t')
plt.ylabel('S(t)')
plt.subplot(122)
plt.plot(sol.t, sol.y[0] - np.exp(-sol.t))
plt.xlabel('t')
plt.ylabel('S(t) - e^(-t)')
plt.tight_layout()
plt.show()