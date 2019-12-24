import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation
t = np.arange (0,100,0.1)

def diff (z, t):
    x, vx, y, vy = z
    dxdt = vx
    dvxdt = -(k*vx**2)/m
    dydt = vy
    dvydt = -m*g
           
    return dxdt, dvxdt, dydt, dvydt

x0 = 0
vx0 = 20
y0 = 0
vy0 = 200

k = 0.0005
m = 1
g = 9.8

z0 = x0, vx0, y0, vy0

solve = odeint(diff, z0, t)
plt.plot(solve[:, 0], solve[:, 2], 'g')
plt.show()