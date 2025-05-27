import math
import matplotlib.pyplot as plt
import numpy as np
import calculus  

def kubna(x):
    return x**3 - 3*x**2 + 2*x

def trig(x):
    return math.sin(x)

def derivacija_kubna(x):
    return 3*x**2 - 6*x + 2

def derivacija_trig(x):
    return math.cos(x)

donja, gornja = 0, 3
broj_tocaka = 100
eps_vrijednosti = [1e-2, 1e-3, 1e-4]
metode = ["three-step", "two-step"]

xs = np.linspace(donja, gornja, broj_tocaka)

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(xs, [derivacija_kubna(x) for x in xs], 'k-', label="analitička derivacija")

for metoda in metode:
    for eps_ in eps_vrijednosti:
        _, deriv = calculus.derivacija_raspon(kubna, donja, gornja, broj_tocaka, eps=eps_, metoda=metoda)
        plt.plot(xs, deriv, label=f"{metoda}, eps={eps_}")

plt.title("deriv. kubne funkcije")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid()

plt.subplot(1, 2, 2)
plt.plot(xs, [derivacija_trig(x) for x in xs], 'k-', label="analitička derivacija")

for metoda in metode:
    for eps_ in eps_vrijednosti:
        _, deriv = calculus.derivacija_raspon(trig, donja, gornja, broj_tocaka, eps=eps_, metoda=metoda)
        plt.plot(xs, deriv, label=f"{metoda}, eps={eps_}")

plt.title("deriv. trig funkcije")
plt.xlabel("x")
plt.ylabel("f'(x)")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()

def test_funkcija(x):
    return x**2 + math.sin(x)

donja_int, gornja_int = 0, math.pi
koraci_integracije = [10, 50, 100, 500]

lijeve_sume = []
desne_sume = []
trapezne_vrijednosti = []

for n in koraci_integracije:
    l, d = calculus.integracija_pravokutna(test_funkcija, donja_int, gornja_int, n)
    t = calculus.integracija_trapez(test_funkcija, donja_int, gornja_int, n)
    lijeve_sume.append(l)
    desne_sume.append(d)
    trapezne_vrijednosti.append(t)

# Pravi graf integracije
plt.figure(figsize=(8, 6))
plt.plot(koraci_integracije, lijeve_sume, 'o-', label="pravokutnav suma")
plt.plot(koraci_integracije, desne_sume, 's-', label="pravokutna suma")
plt.plot(koraci_integracije, trapezne_vrijednosti, '^-', label="trapezna metoda")
plt.axhline(y=2*math.pi, color='k', linestyle='--', label="tocan integral")  
plt.xlabel("broj podjela")
plt.ylabel("vrijednost integrala")
plt.title("numerička integracija funkcije")
plt.legend()
plt.grid()
plt.show()
