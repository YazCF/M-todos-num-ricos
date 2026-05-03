import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Métodos numéricos
def forward_diff(f, x, h):
    return (f(x+h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x-h)) / h

def central_diff(f, x, h):
    return (f(x+h) - f(x-h)) / (2*h)

# Función y derivada analítica
def f(x):
    return np.sin(x)

def df_exact(x):
    return np.cos(x)

# Intervalo
a, b = 0, np.pi
h = 0.1
x = np.arange(a, b+h, h)

# Derivadas
exacta = df_exact(x)
adelante = forward_diff(f, x, h)
atras = backward_diff(f, x, h)
centrada = central_diff(f, x, h)

# Tabla
tabla = pd.DataFrame({
    "x": x,
    "Derivada exacta": exacta,
    "Adelante": adelante,
    "Atrás": atras,
    "Centrada": centrada,
    "Error adelante": np.abs(adelante - exacta),
    "Error atrás": np.abs(atras - exacta),
    "Error centrada": np.abs(centrada - exacta)
})

print(tabla)

# Gráfica derivadas
plt.figure()
plt.plot(x, exacta, 'k', label="Exacta")
plt.plot(x, adelante, 'r--', label="Adelante")
plt.plot(x, atras, 'g-.', label="Atrás")
plt.plot(x, centrada, 'b:', label="Centrada")
plt.title("Ejercicio 1: Derivadas")
plt.xlabel("x")
plt.ylabel("Derivada")
plt.legend()
plt.grid()
plt.show()

# Gráfica errores
plt.figure()
plt.plot(x, np.abs(adelante-exacta), 'r--', label="Error adelante")
plt.plot(x, np.abs(atras-exacta), 'g-.', label="Error atrás")
plt.plot(x, np.abs(centrada-exacta), 'b:', label="Error centrada")
plt.title("Ejercicio 1: Errores")
plt.xlabel("x")
plt.ylabel("Error absoluto")
plt.legend()
plt.grid()
plt.show()
