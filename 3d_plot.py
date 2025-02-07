import numpy as np # Import numerical computing tools
import matplotlib.pyplot as plt # Import plotting tools
from mpl_toolkits.mplot3d import Axes3D # Import 3D plotting tools

x = np.linspace(-5, 5, 50) # x = [-5, -4.8, ..., 4.8, 5] # Create a 1D array
y = np.linspace(-5, 5, 50) # y = [-5, -4.8, ..., 4.8, 5] # Create a 1D array
x, y = np.meshgrid(x, y) # 2D grid for x and y # Create a 2D array
z = x**2 + y**2

fig = plt.figure() # Create a new figure
ax = fig.add_subplot(111, projection='3d') # Add a 3D subplot to the figure
ax.plot_surface(x, y, z)

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_box_aspect(aspect=None, zoom=0.8)
ax.set_title('3D plot of z = x^2 + y^2')

plt.show()