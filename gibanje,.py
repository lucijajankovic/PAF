from particle import Particle
import math
import matplotlib.pyplot as plt

def analiticki_domet(v0, kut_stupnjevi):
    g = 9.81
    kut_rad = math.radians(kut_stupnjevi)
    return (v0**2 * math.sin(2 * kut_rad)) / g

def provjera(v0, kut_stupnjevi, dt=0.01):
    cestica = Particle(v0, kut_stupnjevi)
    numericki = cestica.range(dt)
    analiticki = analiticki_domet(v0, kut_stupnjevi)

    print(f"Numerički domet: {numericki:.2f} m")
    print(f"Analitički domet: {analiticki:.2f} m")
    print(f"Relativna pogreška: {abs(numericki - analiticki) / analiticki * 100:.2f} %")

    cestica.plot_trajectory(dt)

def pogreska(v0, kut_stupnjevi):
    dt_vrijednosti = [0.01, 0.05, 0.1, 0.2, 0.5]
    pogreske = []
    analiticki = analiticki_domet(v0, kut_stupnjevi)

    for dt in dt_vrijednosti:
        cestica = Particle(v0, kut_stupnjevi)
        numericki = cestica.range(dt)
        pogreska = abs(numericki - analiticki) / analiticki
        pogreske.append(pogreska)

    plt.plot(dt_vrijednosti, pogreske, marker="o")
    plt.xlabel("Δt [s]")
    plt.ylabel("Relativna pogreška")
    plt.title("rel. pogreška dometa ovisno o Δt")
    plt.grid()
    plt.show()

provjera(20, 45, dt=0.01)
pogreska(10, 60)
