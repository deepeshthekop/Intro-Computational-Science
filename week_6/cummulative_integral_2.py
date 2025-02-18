import numpy as np
from scipy.integrate import cumulative_trapezoid

x = np.linspace(0, np.pi, 11)
f = np.sin(x)

F_cummulative = cumulative_trapezoid(f, x, initial=0)

print(F_cummulative)