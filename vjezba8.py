import numpy as np
import matplotlib.pyplot as plt

class NabijenaCestica:
    def __init__(self, q, m, r0, v0, E, B):
        self.q = q
        self.m = m
        self.r = np.array(r0, dtype=float)
        self.v = np.array(v0, dtype=float)
        self.E = np.array(E, dtype=float)
        self.B = np.array(B, dtype=float)

    def akceleracija(self, v):
        return (self.q / self.m) * (self.E + np.cross(v, self.B))

    def euler(self, dt, t_max):
        r = self.r.copy()
        v = self.v.copy()
        rs = [r.copy()]
        ts = [0]
        t = 0
        while t < t_max:
            a = self.akceleracija(v)
            v += a * dt
            r += v * dt
            rs.append(r.copy())
            t += dt
            ts.append(t)
        return np.array(rs), np.array(ts)

    def rk4(self, dt, t_max):
        r = self.r.copy()
        v = self.v.copy()
        rs = [r.copy()]
        ts = [0]
        t = 0
        while t < t_max:
            def derivs(v):
                return self.akceleracija(v)

            k1v = derivs(v)
            k1r = v

            k2v = derivs(v + 0.5 * dt * k1v)
            k2r = v + 0.5 * dt * k1v

            k3v = derivs(v + 0.5 * dt * k2v)
            k3r = v + 0.5 * dt * k2v

            k4v = derivs(v + dt * k3v)
            k4r = v + dt * k3v

            v += (dt / 6) * (k1v + 2 * k2v + 2 * k3v + k4v)
            r += (dt / 6) * (k1r + 2 * k2r + 2 * k3r + k4r)

            rs.append(r.copy())
            t += dt
            ts.append(t)
        return np.array(rs), np.array(ts)

# parametri
q_e = -1
q_p = 1
m = 1
E = [0, 0, 0]
B = [0, 0, 1]
r0 = [0, 0, 0]
v0 = [0.1, 0.1, 0.1]
dt = 0.01
t_max = 100

# elektron i pozitron
elektron = NabijenaCestica(q_e, m, r0, v0, E, B)
pozitron = NabijenaCestica(q_p, m, r0, v0, E, B)

# trajektorije
r_e, _ = elektron.rk4(dt, t_max)
r_p, _ = pozitron.rk4(dt, t_max)

# prikaz
fig = plt.figure(figsize=(12, 6))
ax1 = fig.add_subplot(121, projection='3d')
ax1.plot(r_e[:,0], r_e[:,1], r_e[:,2])
ax1.set_title('trajektorija elektrona')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_zlabel('z')

ax2 = fig.add_subplot(122, projection='3d')
ax2.plot(r_p[:,0], r_p[:,1], r_p[:,2])
ax2.set_title('trajektorija pozitrona')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_zlabel('z')

plt.tight_layout()
plt.show()
