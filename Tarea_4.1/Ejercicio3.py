import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ===== CONFIGURACIÓN PARA VER BIEN LA TABLA =====
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', None)
pd.set_option('display.float_format', '{:.6f}'.format)

# ===== MÉTODOS DE DIFERENCIACIÓN NUMÉRICA =====
def forward_diff(f, x, h):
    return (f(x + h) - f(x)) / h

def backward_diff(f, x, h):
    return (f(x) - f(x - h)) / h

def central_diff(f, x, h):
    return (f(x + h) - f(x - h)) / (2*h)

# ===== FUNCIÓN Y DERIVADA ANALÍTICA =====
def f(x):
    return x**3 - 2*x**2 + x

def df_exact(x):
    return 3*x**2 - 4*x + 1

# ===== INTERVALO =====
a, b = -1, 2
h = 0.2
x = np.arange(a, b + h, h)

# ===== DERIVADAS =====
exacta = df_exact(x)
adelante = forward_diff(f, x, h)
atras = backward_diff(f, x, h)
centrada = central_diff(f, x, h)

# ===== TABLA COMPLETA =====
tabla = pd.DataFrame({
    "x": x,
    "Derivada exacta": exacta,
    "Derivada hacia adelante": adelante,
    "Derivada hacia atrás": atras,
    "Derivada centrada": centrada,
    "Error absoluto adelante": np.abs(adelante - exacta),
    "Error absoluto atrás": np.abs(atras - exacta),
    "Error absoluto centrada": np.abs(centrada - exacta)
})

print(tabla)

# ===== GRÁFICA DE DERIVADAS =====
plt.figure(figsize=(10, 6))
plt.plot(x, exacta, 'k', label="Derivada exacta")
plt.plot(x, adelante, 'r--', label="Hacia adelante")
plt.plot(x, atras, 'g-.', label="Hacia atrás")
plt.plot(x, centrada, 'b:', label="Centrada")
plt.xlabel("x")
plt.ylabel("Derivada")
plt.title("Ejercicio 3: Comparación de derivadas")
plt.legend()
plt.grid()
plt.show()

# ===== GRÁFICA DE ERRORES =====
plt.figure(figsize=(10, 6))
plt.plot(x, np.abs(adelante - exacta), 'r--', label="Error adelante")
plt.plot(x, np.abs(atras - exacta), 'g-.', label="Error atrás")
plt.plot(x, np.abs(centrada - exacta), 'b:', label="Error centrada")
plt.xlabel("x")
plt.ylabel("Error absoluto")
plt.title("Ejercicio 3: Errores numéricos")
plt.legend()
plt.grid()
plt.show()

# ===== GUARDAR TABLA (RECOMENDADO) =====
tabla.to_excel("Ejercicio3_tabla.xlsx", index=False)