import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 
fig, ax = plt.subplots()
anim_object, = plt.plot([], [], marker='o')
def circle_m(R, t):
    t = np.arange(-2*np.pi,2*np.pi, 0.1)
    x = R*(t - np.sin(t))
    y = R*(1 - np.cos(t))
    return x,y

edge = 4
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    anim_object.set_data(circle_m(R=3, t=i))

ani = animation.FuncAnimation(fig,
                              animate,
                              frames=np.arange(-2*np.pi,2*np.pi, 0.1),
                              interval=300)

circ = circle_m(R=3, t = np.arange(-2*np.pi,2*np.pi, 0.1))
plt.plot(circ[0], circ[1])
ani.save('animat.gif')