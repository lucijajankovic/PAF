from particle import Particle
import math
import matplotlib.pyplot as plt

# Analitički domet
def analytical_range(v0, theta_deg):
    theta = math.radians(theta_deg)
    g = 9.81
    return (v0**2 * math.sin(2 * theta)) / g

# 1. Provjera dometa za jedan konkretan slučaj
v0 = 20  # m/s
theta = 45  # stupnjeva

p = Particle(v0, theta)
numeric = p.range(dt=0.01)
analytic = analytical_range(v0, theta)

print(f"Numerički domet: {numeric:.2f} m")
print(f"Analitički domet: {analytic:.2f} m")
print(f"Relativna pogreška: {abs(numeric - analytic) / analytic * 100:.2f} %")

p.plot_trajectory()

# 2. Pogreška za različite ∆t
def plot_relative_error(v0, theta_deg):
    dt_values = [0.001 * i for i in range(1, 51)]
    errors = []
    analytic = analytical_range(v0, theta_deg)

    for dt in dt_values:
        p = Particle(v0, theta_deg)
        numeric = p.range(dt)
        error = abs(numeric - analytic) / analytic
        errors.append(error)

    plt.plot(dt_values, errors)
    plt.xlabel("∆t [s]")
    plt.ylabel("Relativna pogreška")
    plt.title("Relativna pogreška u funkciji ∆t")
    plt.grid()
    plt.show()

plot_relative_error(10, 60)
