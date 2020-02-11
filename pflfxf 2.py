import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt 
import numpy as np

fig = plt.figure()
ax = p3.Axes3D(fig)

a = 15
b = 25
c = 30

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

x = a * np.outer(np.cos(phi), np.cosh(theta))
y = b * np.outer(np.sin(phi), np.cosh(theta))
z = c * np.outer(np.ones(np.size(phi)), np.cosh(theta))


ax.plot_surface(x, y, z, color="r")


a = 15
b = 25
c = -30

phi = np.linspace(0, 2 * np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

x = a * np.outer(np.cos(phi), np.cosh(theta))
y = b * np.outer(np.sin(phi), np.cosh(theta))
z = c * np.outer(np.ones(np.size(phi)), np.cosh(theta))


ax.plot_surface(x, y, z, color="r")
plt.show()
