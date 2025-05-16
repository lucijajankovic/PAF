import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, v0, theta_deg, x0=0, y0=0):
        self.v0 = v0
        self.theta = math.radians(theta_deg)
        self.x = x0
        self.y = y0
        self.vx = v0 * math.cos(self.theta)
        self.vy = v0 * math.sin(self.theta)
        self.x0 = x0
        self.y0 = y0
        self.t = 0
        self.g = 9.81
        self.trajectory = [(x0, y0)]

    def reset(self):
        self.__init__(self.v0, math.degrees(self.theta), self.x0, self.y0)

    def __move(self, dt):
        self.x += self.vx * dt
        self.vy -= self.g * dt
        self.y += self.vy * dt
        self.t += dt
        self.trajectory.append((self.x, self.y))

    def range(self, dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self, dt=0.01):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        x_vals, y_vals = zip(*self.trajectory)
        plt.plot(x_vals, y_vals)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('Putanja projektila')
        plt.grid()
        plt.show()

