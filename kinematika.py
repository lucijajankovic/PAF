import numpy as np
import matplotlib.pyplot as plt

def jednoliko_gibanje(F, m, t_max=10, dt=0.1):
    a = F / m  # Konstantno ubrzanje
    t = np.arange(0, t_max, dt)
    v = a * t
    x = 0.5 * a * t**2
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(3, 1, 1)
    plt.plot(t, x, label='x-t', color='r')
    plt.xlabel('vrjeme')
    plt.ylabel('položaj')
    plt.title('x - t')
    plt.grid()
    
    plt.subplot(3, 1, 2)
    plt.plot(t, v, label='v-t', color='g')
    plt.xlabel('vrijeme')
    plt.ylabel('brzina')
    plt.title('v - t ')
    plt.grid()
    
    plt.subplot(3, 1, 3)
    plt.plot(t, np.full_like(t, a), label='a-t', color='b')
    plt.xlabel('vrijeme')
    plt.ylabel('ubrzanje')
    plt.title('a - t')
    plt.grid()
    
    plt.tight_layout()
    plt.show()

def kosi_hitac(v0, theta, t_max=10, dt=0.1, g=9.81):
    theta_rad = np.radians(theta)
    v0x = v0 * np.cos(theta_rad)  
    v0y = v0 * np.sin(theta_rad)  
    
    t = np.arange(0, t_max, dt)
    x = v0x * t
    y = v0y * t - 0.5 * g * t**2
    t_pad = (2 * v0y) / g
    maska = t <= t_pad
    x = x[maska]
    y = y[maska]
    t = t[maska]
    
    plt.figure(figsize=(10, 5))
    
    plt.subplot(3, 1, 1)
    plt.plot(x, y, label='x-y', color='r')
    plt.xlabel('x')
    plt.ylabel('y ')
    plt.title('x - y')
    plt.grid()
    
    plt.subplot(3, 1, 2)
    plt.plot(t, x, label='x-t', color='g')
    plt.xlabel('vrijeme')
    plt.ylabel('x ')
    plt.title('x - t')
    plt.grid()
    
    plt.subplot(3, 1, 3)
    plt.plot(t, y, label='y-t', color='b')
    plt.xlabel('vrijeme')
    plt.ylabel('y (m)')
    plt.title('y - t ')
    plt.grid()
    
    plt.tight_layout()
    plt.show()
