import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
t = np.arange (0, 100, 0.1)

def diff (z, t):
    x, vx, y, vy = z
    dxdt = vx
    dvxdt = (f2*np.cos(2*np.pi/180*60)+f3*np.cos(2*np.pi/180*30)+f4)/m
    dydt = vy
    dvydt = (f1+f2*np.cos(2*np.pi/180*30)+f3*np.cos(2*np.pi/180*60))/m
    return dxdt, dvxdt, dydt, dvydt

x0 = 0
vx0 = -2
y0 = 0
vy0 = -20

f1 = 1
f2 = 2
f3 = 3
f4 = 4
m = 1

z0 = x0, vx0, y0, vy0

solve = odeint(diff, z0, t)
plt.plot(solve[:, 0], solve[:, 2], 'g')
plt.show()