import numpy as np
import matplotlib.pyplot as plt
def Cicloida(R=5, t=1):
    t = np.arange(-2*np.pi,2*np.pi, 0.1)
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
    plt.plot(x, y, label='Cicloida')
    plt.xlim(-10*np.pi,10*np.pi)
    plt.ylim(-10*np.pi,10*np.pi)
    plt.legend()
    plt.show()
Cicloida()  