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

k = 0.5
a, b = 0, 2
n_values = [6, 10, 20, 30]

def dTdx(x):
    return k * (-100 * x)

Q_exacta = -100

datos = []

for n in n_values:
    Q_simpson = simpson_rule(dTdx, a, b, n)
    error = abs(Q_simpson - Q_exacta)
    datos.append([n, Q_simpson, Q_exacta, error])

tabla = pd.DataFrame(datos, columns=["n", "Simpson", "Exacta", "Error"])
print("\nEJERCICIO 3")
print(tabla)

for n in n_values:
    x = np.linspace(a, b, 200)
    plt.plot(x, dTdx(x))
    plt.fill_between(x, dTdx(x), alpha=0.3)
    plt.scatter(np.linspace(a, b, n+1), dTdx(np.linspace(a, b, n+1)), color="red")
    plt.title(f"Flujo de calor (n={n})")
    plt.xlabel("x")
    plt.ylabel("Q")
    plt.grid()
    plt.savefig(f"ejercicio3_n{n}.png")
    plt.show()

plt.plot(tabla["n"], tabla["Error"], marker="o")
plt.xlabel("n")
plt.ylabel("Error absoluto")
plt.title("Error vs n - Ejercicio 3")
plt.grid()
plt.savefig("ejercicio3_error.png")
plt.show()