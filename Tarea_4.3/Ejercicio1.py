import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Regla de Simpson
def simpson_rule(f, a, b, n):
    if n % 2 == 1:
        raise ValueError("n debe ser par")
    h = (b - a) / n
    x = np.linspace(a, b, n + 1)
    fx = f(x)
    return (h/3)*(fx[0] + 2*np.sum(fx[2:n:2]) + 4*np.sum(fx[1:n:2]) + fx[n])

# Datos
k = 200
a, b = 0.1, 0.3
n_values = [6, 10, 20, 30]

def fuerza(x):
    return k * x

# Solución analítica
W_exacta = k/2 * (b**2 - a**2)

# Tabla
datos = []

for n in n_values:
    W_simpson = simpson_rule(fuerza, a, b, n)
    error = abs(W_simpson - W_exacta)
    datos.append([n, W_simpson, W_exacta, error])

tabla = pd.DataFrame(datos, columns=["n", "Simpson", "Exacta", "Error"])
print("\nEJERCICIO 1")
print(tabla)

# Gráficas
for n in n_values:
    x = np.linspace(a, b, 200)
    plt.plot(x, fuerza(x))
    plt.fill_between(x, fuerza(x), alpha=0.3)
    plt.scatter(np.linspace(a, b, n+1), fuerza(np.linspace(a, b, n+1)), color="red")
    plt.title(f"Trabajo en un resorte (n={n})")
    plt.xlabel("x")
    plt.ylabel("F(x)")
    plt.grid()
    plt.savefig(f"ejercicio1_n{n}.png")
    plt.show()

# Error vs n
plt.plot(tabla["n"], tabla["Error"], marker="o")
plt.xlabel("n")
plt.ylabel("Error absoluto")
plt.title("Error vs n - Ejercicio 1")
plt.grid()
plt.savefig("ejercicio1_error.png")
plt.show()