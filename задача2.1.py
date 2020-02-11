import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.pyplot as plt 
import numpy as np
from matplotlib import animation

fig = plt.figure()
ax = p3.Axes3D(fig)

phi = np.linspace(0, np.pi, 100)
theta = np.linspace(0, 2 * np.pi, 100)

h = 0.5
N = 100

x1 = np.outer(phi, np.cos(theta))
y1 = np.outer(phi, np.sin(theta))
z1 = h * np.outer(np.ones(np.size(theta)), theta)
ax.plot_surface(x1, y1, z1, color="r")
plt.show()

x = phi * np.cos(theta)
y = phi * np.sin(theta)
z = h * theta

ball, = ax.plot(x, y, z, 'o', color="b")
line, = ax.plot(x, y, z, '-', color="y")

def animation_func(i):
    ball.set_data(x[i], y[i])
    ball.set_3d_properties(z[i])
    
    line.set_data(x[:i], y[:i])
    line.set_3d_properties(z[:i])

ax.set_xlim3d([-4.0, 4.0])
ax.set_xlabel('X')

ax.set_xlim3d([-4.0, 4.0])
ax.set_xlabel('Y')
    
ax.set_xlim3d([-4.0, 4.0])
ax.set_xlabel('Z')
   
#ax.plot_surface(x, y, z, color="r")
ani = animation.FuncAnimation(fig, animation_func, N, interval = 50)
ani.save('dvizh.gif')

#plt.show()