import numpy as np

class Projectile:
    def __init__(self, x0, y0, v0, kut_stupnjevi, m, c_d, A, rho=1.225, g=9.81):
        self.x = x0
        self.y = y0
        self.v0 = v0
        self.kut = np.radians(kut_stupnjevi)
        self.vx = v0 * np.cos(self.kut)
        self.vy = v0 * np.sin(self.kut)
        self.m = m
        self.c_d = c_d
        self.A = A
        self.rho = rho
        self.g = g

    def _sila_otpora(self, vx, vy):
        v = np.sqrt(vx**2 + vy**2)
        Fd = 0.5 * self.c_d * self.rho * self.A * v**2
        if v == 0:
            return 0, 0
        Fdx = -Fd * vx / v
        Fdy = -Fd * vy / v
        return Fdx, Fdy

    def euler_step(self, dt):
        Fdx, Fdy = self._sila_otpora(self.vx, self.vy)
        ax = Fdx / self.m
        ay = Fdy / self.m - self.g

        self.vx += ax * dt
        self.vy += ay * dt

        self.x += self.vx * dt
        self.y += self.vy * dt

    def simulate_euler(self, t_max, dt):
        t = 0
        xs = []
        ys = []
        while self.y >= 0 and t <= t_max:
            xs.append(self.x)
            ys.append(self.y)
            self.euler_step(dt)
            t += dt
        return np.array(xs), np.array(ys)

    def _izvod(self, stanje):
        x, y, vx, vy = stanje
        Fdx, Fdy = self._sila_otpora(vx, vy)
        ax = Fdx / self.m
        ay = Fdy / self.m - self.g
        return np.array([vx, vy, ax, ay])

    def rk4_step(self, dt, stanje):
        k1 = self._izvod(stanje)
        k2 = self._izvod(stanje + 0.5 * dt * k1)
        k3 = self._izvod(stanje + 0.5 * dt * k2)
        k4 = self._izvod(stanje + dt * k3)
        return stanje + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4)

    def simulate_rk4(self, t_max, dt):
        t = 0
        stanje = np.array([self.x, self.y, self.vx, self.vy])
        xs = []
        ys = []
        while stanje[1] >= 0 and t <= t_max:
            xs.append(stanje[0])
            ys.append(stanje[1])
            stanje = self.rk4_step(dt, stanje)
            t += dt
        return np.array(xs), np.array(ys)
