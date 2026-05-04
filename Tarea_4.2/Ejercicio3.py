import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Función
def f(x):
    return np.sin(x)

# Regla del trapecio
def trapezoidal_rule(a, b, n):
    x = np.linspace(a, b, n+1)
    y = f(x)
    h = (b - a) / n
    I = (h/2)*(y[0] + 2*np.sum(y[1:-1]) + y[-1])
    return I, x, y

# Parámetros
a, b = 0, np.pi
n_values = [4, 8, 16]
exact = 2

data = []

for n in n_values:
    I, _, _ = trapezoidal_rule(a, b, n)
    error = abs(I - exact)
    data.append([n, I, exact, error])

tabla = pd.DataFrame(
    data,
    columns=["n", "Aproximación", "Exacta", "Error"]
)

print("\nTABLA DE RESULTADOS - EJERCICIO 3")
print(tabla)

n_plot = 8
I, x, y = trapezoidal_rule(a, b, n_plot)

x_fine = np.linspace(a, b, 400)

plt.figure(figsize=(8,5))
plt.plot(x_fine, f(x_fine), 'r', linewidth=2, label='f(x)')
plt.fill_between(x, y, color='blue', alpha=0.3, label='Área por trapecios')
plt.plot(x, y, 'bo-', label='Puntos de integración')

plt.title("Ejercicio 3: Regla del Trapecio")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()

plt.savefig("ejercicio3.png")
plt.show()