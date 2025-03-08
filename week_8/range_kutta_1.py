import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

F = lambda t, s: np.cos(t) # s'(t) = cos(t)

t_eval = np.arange(0, np.pi, 0.1) # t = 0, 0.1, 0.2, ..., 3.1

sol = solve_ivp(F, [0, np.pi], [0], t_eval=t_eval) # s(0) = 0 and t = 0 to 3.1 with step 0.1

plt.figure(figsize=(12, 4)) # width, height in inches
plt.subplot(121) # 1 row, 2 columns, 1st subplot
plt.plot(sol.t, sol.y[0]) # S(t)
plt.xlabel('t')
plt.ylabel('S(t)')
plt.subplot(122) # 1 row, 2 columns, 2nd subplot
plt.plot(sol.t, sol.y[0] - np.sin(sol.t)) # S(t) - sin(t)
plt.xlabel('t')
plt.ylabel('S(t) - sin(t)')
plt.tight_layout()
plt.show()