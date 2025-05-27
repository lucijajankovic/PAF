import numpy as np
import matplotlib.pyplot as plt

G = 6.67408e-11
AU = 1.496e11
day = 86400
year = 365.242 * day

M_sunce = 1.989e30
M_zemlja = 5.9742e24

r_sunce_0 = np.array([0.0, 0.0])
r_zemlja_0 = np.array([AU, 0.0])

v_sunce_0 = np.array([0.0, 0.0])
v_zemlja_0 = np.array([0.0, 29783.0])

dt = 60 * 60
n_steps = int(year / dt)

r_sunce = np.zeros((n_steps, 2))
v_sunce = np.zeros((n_steps, 2))
r_zemlja = np.zeros((n_steps, 2))
v_zemlja = np.zeros((n_steps, 2))

r_sunce[0] = r_sunce_0
v_sunce[0] = v_sunce_0
r_zemlja[0] = r_zemlja_0
v_zemlja[0] = v_zemlja_0

for i in range(n_steps - 1):
    r_rel = r_zemlja[i] - r_sunce[i]
    dist = np.linalg.norm(r_rel)
    force_dir = r_rel / dist
    force_mag = G * M_sunce * M_zemlja / dist**2
    force = -force_mag * force_dir

    a_zemlja = force / M_zemlja
    a_sunce = -force / M_sunce

    v_zemlja[i + 1] = v_zemlja[i] + a_zemlja * dt
    v_sunce[i + 1] = v_sunce[i] + a_sunce * dt

    r_zemlja[i + 1] = r_zemlja[i] + v_zemlja[i + 1] * dt
    r_sunce[i + 1] = r_sunce[i] + v_sunce[i + 1] * dt

print("Sunce x min/max:", r_sunce[:,0].min(), r_sunce[:,0].max())
print("Sunce y min/max:", r_sunce[:,1].min(), r_sunce[:,1].max())

faktor = 5000
plt.plot(r_sunce[:, 0]*faktor*1e-9, r_sunce[:, 1]*faktor*1e-9, label='Sunce (prikaz x5000)')
plt.plot(r_zemlja[:, 0]*1e-9, r_zemlja[:, 1]*1e-9, label='Zemlja')
plt.xlabel('x [10^9 m]')
plt.ylabel('y [10^9 m]')
plt.axis('equal')
plt.legend()
plt.title('putanje zemlje i sunca ')
plt.grid(True)
plt.show()
