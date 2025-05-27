import math
import matplotlib.pyplot as plt

class Cestica:
    def __init__(self, pocetna_brzina, theta_stupnjevi, x0=0, y0=0):
        self.v0 = pocetna_brzina
        self.theta = math.radians(theta_stupnjevi)
        self.x = x0
        self.y = y0
        self.vx = self.v0 * math.cos(self.theta)
        self.vy = self.v0 * math.sin(self.theta)
        self.g = 9.81
        self.x_koordinate = [x0]
        self.y_koordinate = [y0]

    def resetiraj(self):
        self.x = 0
        self.y = 0
        self.x_koordinate = [0]
        self.y_koordinate = [0]

    def __pomakni(self, dt):
        self.vy -= self.g * dt
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.x_koordinate.append(self.x)
        self.y_koordinate.append(self.y)

    def domet(self, dt):
        self.resetiraj()
        while self.y >= 0:
            self.__pomakni(dt)
        return self.x

    def nacrtaj_putanju(self, dt):
        self.resetiraj()
        while self.y >= 0:
            self.__pomakni(dt)
        plt.plot(self.x_koordinate, self.y_koordinate)
        plt.xlabel("x [m]")
        plt.ylabel("y [m]")
        plt.title("Putanja čestice")
        plt.grid()
        plt.show()
