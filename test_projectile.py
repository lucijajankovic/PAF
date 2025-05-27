import matplotlib.pyplot as plt
from projectile import Projectile
import numpy as np

x0, y0 = 0, 0
v0 = 50
kut = 45
m = 1.0
c_d = 0.47
A = 0.05

t_max = 10
dt = 0.01

proj_euler = Projectile(x0, y0, v0, kut, m, c_d, A)
xs_euler, ys_euler = proj_euler.simulate_euler(t_max, dt)

proj_rk4 = Projectile(x0, y0, v0, kut, m, c_d, A)
xs_rk4, ys_rk4 = proj_rk4.simulate_rk4(t_max, dt)

plt.figure(figsize=(10,6))
plt.plot(xs_euler, ys_euler, label='eulerova metoda')
plt.plot(xs_rk4, ys_rk4, label='runge-Kutta 4. reda')
plt.xlabel('x')
plt.ylabel('y')
plt.title('kos hitac s otporom zraka')
plt.legend()
plt.grid()
plt.show()
