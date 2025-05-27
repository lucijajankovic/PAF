import numpy as np
import matplotlib.pyplot as plt
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])  
M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])          

n = len(phi)

xy = np.sum(phi * M)
x2 = np.sum(phi**2)
Dt = xy / x2

y2 = np.sum(M**2)
sigma_Dt = np.sqrt((1/n) * (y2 / x2 - Dt**2))

print(f"Modul torzije Dt: {Dt:.4f} Nm/rad")
print(f"Standardna devijacija σ_Dt: {sigma_Dt:.4f} Nm/rad")

plt.scatter(phi, M, label="Eksperimentalni podaci")
plt.plot(phi, Dt * phi, color='red', label=f"Fit: M = {Dt:.4f} φ")
plt.xlabel("φ (rad)")
plt.ylabel("M (Nm)")
plt.title("Linear Regression: M = Dt · φ")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
