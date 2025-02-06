# %%
import numpy as np
import matplotlib.pyplot as plt

x = [0, 1, 2, 3]
y = [0, 1, 4, 9]

plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of y = x^2') 
plt.show()


# %%
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 100) # x = [-5, -4.9, -4.8, ..., 4.9, 5]
y = x**2

plt.plot(x, y, "r-.") # red, dashed line
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Plot of y = x^2')
plt.show()


# %%
import numpy as np
# from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 50) # x = [-5, -4.8, ..., 4.8, 5]
y = np.linspace(-5, 5, 50) # y = [-5, -4.8, ..., 4.8, 5]
x, y = np.meshgrid(x, y) # 2D grid for x and y
z = x**2 + y**2

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x, y, z)
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_box_aspect(aspect=None, zoom=0.8)
ax.set_title('3D plot of z = x^2 + y^2')
plt.show()