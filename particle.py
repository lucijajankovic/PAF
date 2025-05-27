import math
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, pocetna_brzina, kut_otklona_stupnjevi, x0=0, y0=0):
        self.v0 = pocetna_brzina
        self.theta = math.radians(kut_otklona_stupnjevi)
        self.x = x0
        self.y = y0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)
        self.g = 9.81
        self.x_koordinate = [x0]
        self.y_koordinate = [y0]

    def reset(self):
        self.x = 0
        self.y = 0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)
        self.x_koordinate = [self.x]
        self.y_koordinate = [self.y]

    def __move(self, dt):
        self.vy -= self.g * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.x_koordinate.append(self.x)
        self.y_koordinate.append(self.y)

    def range(self, dt):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self, dt):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        plt.plot(self.x_koordinate, self.y_koordinate)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("putanja")
        plt.grid()
        plt.show()
