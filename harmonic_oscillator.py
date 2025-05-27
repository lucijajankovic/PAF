import numpy as np

class HarmonicOscillator:
    def __init__(self, m, k, x0, v0):
        self.m = m
        self.k = k
        self.x = x0
        self.v = v0
        self.a = -k/m * x0

    def analiticko_rjesenje(self, t):
        omega = np.sqrt(self.k / self.m)
        A = self.x
        B = self.v / omega
        return A * np.cos(omega * t) + B * np.sin(omega * t)

    def korak(self, dt):
        a = -self.k / self.m * self.x
        self.v += a * dt
        self.x += self.v * dt
        self.a = a

    def gibanje(self, T, dt):
        n = int(T / dt)
        xs = np.zeros(n)
        vs = np.zeros(n)
        as_ = np.zeros(n)
        ts = np.linspace(0, T, n)
        for i in range(n):
            xs[i] = self.x
            vs[i] = self.v
            as_[i] = self.a
            self.korak(dt)
        return ts, xs, vs, as_

    def period(self, T, dt):
        ts, xs, vs, _ = self.gibanje(T, dt)
        prethodni_x = xs[0]
        prethodni_v = vs[0]
        crossing_times = []
        for i in range(1, len(xs)):
            if (prethodni_x < 0 and xs[i] >= 0) and vs[i] > 0:
                t_cross = ts[i-1] + (0 - prethodni_x) * (ts[i] - ts[i-1]) / (xs[i] - prethodni_x)
                crossing_times.append(t_cross)
            prethodni_x = xs[i]
            prethodni_v = vs[i]
        if len(crossing_times) < 2:
            return None
        periodi = np.diff(crossing_times)
        prosjecni_period = np.mean(periodi)
        return 2 * prosjecni_period
