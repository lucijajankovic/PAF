# Zadatak 1:
print("Hello world!")

# Zadatak 3: 
def unos(ime):
    while True:
        try:
            x, y = map(float, input(f"Unesi koordinate {ime} (x y): ").split())
            return x, y
        except ValueError:
            print("Pogrešan unos! Molimo unesite dvije brojeve odvojene razmakom.")

def izracunaj(x1, y1, x2, y2):
    if x1 == x2:
        print(f"Jednadžba pravca: x = {x1}")
    else:
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        print(f"Jednadžba pravca: y = {k:.2f}x + {l:.2f}")

x1, y1 = unos("točke A")
x2, y2 = unos("točke B")
izracunaj(x1, y1, x2, y2)

# Zadatak 4: 
def jednadzba_pravca(x1, y1, x2, y2):
    if x1 == x2:
        return f"x = {x1}"
    k = (y2 - y1) / (x2 - x1)
    l = y1 - k * x1
    return f"y = {k:.2f}x + {l:.2f}"

print(jednadzba_pravca(x1, y1, x2, y2))

# Zadatak 5: Prikaz i spremanje grafa
import matplotlib.pyplot as plt

def iscrtaj_pravac(x1, y1, x2, y2, prikazi=True, naziv_datoteke="graf.pdf"):
    if x1 == x2:
        x = [x1, x1]
        y = [min(y1, y2) - 1, max(y1, y2) + 1]
    else:
        x = [x1, x2]
        k = (y2 - y1) / (x2 - x1)
        l = y1 - k * x1
        y = [k * x1 + l, k * x2 + l]
    
    plt.plot(x, y, 'r-')
    plt.scatter([x1, x2], [y1, y2])
    
    
    if prikazi:
        plt.show()
    else:
        plt.savefig(naziv_datoteke)
        print(f"Graf je spremljen kao {naziv_datoteke}")

naziv_datoteke = input("Unesite naziv datoteke: ")
iscrtaj_pravac(x1, y1, x2, y2, prikazi=False, naziv_datoteke=naziv_datoteke)
