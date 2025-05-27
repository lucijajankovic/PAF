import numpy as np

def derivacija(funkcija, tocka, eps=1e-5, metoda="three-step"):
    
    if metoda == "three-step":
        return (funkcija(tocka + eps) - funkcija(tocka - eps)) / (2 * eps)
    elif metoda == "two-step":
        return (funkcija(tocka) - funkcija(tocka - eps)) / eps
    else:
        raise ValueError(" 'three-step' ili 'two-step'.")

def derivacija_raspon(funkcija, donja_granica, gornja_granica, broj_tocaka=100, eps=1e-5, metoda="three-step"):
   
    xs = np.linspace(donja_granica, gornja_granica, broj_tocaka)
    derivacije = [derivacija(funkcija, x, eps=eps, metoda=metoda) for x in xs]
    return xs, derivacije

def integracija_pravokutna(funkcija, donja_granica, gornja_granica, broj_podjela=100):
  
    dx = (gornja_granica - donja_granica) / broj_podjela
    xs = np.linspace(donja_granica, gornja_granica, broj_podjela + 1)

    lijeva_suma = sum(funkcija(xs[i]) for i in range(broj_podjela)) * dx
    desna_suma = sum(funkcija(xs[i]) for i in range(1, broj_podjela + 1)) * dx

    return lijeva_suma, desna_suma

def integracija_trapez(funkcija, donja_granica, gornja_granica, broj_podjela=100):
   
    dx = (gornja_granica - donja_granica) / broj_podjela
    xs = np.linspace(donja_granica, gornja_granica, broj_podjela + 1)

    suma = 0.5 * (funkcija(xs[0]) + funkcija(xs[-1]))
    suma += sum(funkcija(x) for x in xs[1:-1])
    return suma * dx

