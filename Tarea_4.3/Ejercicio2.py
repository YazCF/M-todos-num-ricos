import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    return (h/3)*(fx[0] + 2*np.sum(fx[2:n:2]) + 4*np.sum(fx[1:n:2]) + fx[n])

C = 1e-6
a, b = 0, 5
n_values = [6, 10, 20, 30]

def voltaje(t):
    return C * 100 * np.exp(-2*t)

Q_exacta = C * 50 * (1 - np.exp(-10))

datos = []

for n in n_values:
    Q_simpson = simpson_rule(voltaje, a, b, n)
    error = abs(Q_simpson - Q_exacta)
    datos.append([n, Q_simpson, Q_exacta, error])

tabla = pd.DataFrame(datos, columns=["n", "Simpson", "Exacta", "Error"])
print("\nEJERCICIO 2")
print(tabla)

for n in n_values:
    t = np.linspace(a, b, 200)
    plt.plot(t, voltaje(t))
    plt.fill_between(t, voltaje(t), alpha=0.3)
    plt.scatter(np.linspace(a, b, n+1), voltaje(np.linspace(a, b, n+1)), color="red")
    plt.title(f"Carga en el capacitor (n={n})")
    plt.xlabel("t")
    plt.ylabel("Q(t)")
    plt.grid()
    plt.savefig(f"ejercicio2_n{n}.png")
    plt.show()

plt.plot(tabla["n"], tabla["Error"], marker="o")
plt.xlabel("n")
plt.ylabel("Error absoluto")
plt.title("Error vs n - Ejercicio 2")
plt.grid()
plt.savefig("ejercicio2_error.png")
plt.show()