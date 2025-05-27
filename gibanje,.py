from Particle import Cestica
import math
import matplotlib.pyplot as plt

g = 9.81 

def domet(v0, theta_stupnjevi):
    theta_radiani = math.radians(theta_stupnjevi)
    return (v0**2 * math.sin(2 * theta_radiani)) / g

def provjera(v0, theta_stupnjevi, dt=0.01):
    cestica = Cestica(v0, theta_stupnjevi)
    numericki = cestica.domet(dt)
    analiticki = domet(v0, theta_stupnjevi)

    print(f"numerički domet: {numericki:.2f} m")
    print(f"analitički domet: {analiticki:.2f} m")
    print(f"pogreška: {abs(numericki - analiticki) / analiticki * 100:.2f} %")

    cestica.nacrtaj(dt)

def pogreska(v0, theta_stupnjevi):
    koraci = [0.01, 0.05, 0.1, 0.2, 0.5]
    pogreske = []
    analiticki = domet(v0, theta_stupnjevi)

    for dt in koraci:
        cestica = Cestica(v0, theta_stupnjevi)
        numericki = cestica.domet(dt)
        pogreska = abs(numericki - analiticki) / analiticki
        pogreske.append(pogreska)

    plt.plot(koraci, pogreske, marker="o")
    plt.xlabel("Δt [s]")
    plt.ylabel("relativna pogreška")
    plt.title("rel. pogreška u ovisnosti o Δt")
    plt.grid()
    plt.show()


provjera(20, 45, dt=0.01)
pogreska(10, 60)
