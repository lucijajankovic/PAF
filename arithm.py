#a)
mjerenja = [10.2, 9.8, 10.1, 10.5, 9.9, 10.0, 10.3, 9.7, 10.4, 10.1]
n = len(mjerenja)

suma = 0
for x in mjerenja:
    suma += x
sredina = suma / n

odstupanja_kvadrat = 0
for x in mjerenja:
    odstupanja_kvadrat += (x - sredina) ** 2
sigma = (odstupanja_kvadrat / (n * (n - 1))) ** 0.5

print("Mjerenja:", mjerenja)
print(f"Aritmetička sredina: {sredina:.2f}")
print(f"Standardna devijacija: {sigma:.4f}")

#b)

import numpy as np

mjerenja = np.array([10.2, 9.8, 10.1, 10.5, 9.9, 10.0, 10.3, 9.7, 10.4, 10.1])
n = len(mjerenja)

sredina = np.mean(mjerenja)
sigma = np.sqrt(np.sum((mjerenja - sredina) ** 2) / (n * (n - 1)))

print("Mjerenja:", mjerenja)
print(f"Aritmetička sredina: {sredina:.2f}")
print(f"Standardna devijacija: {sigma:.4f}")