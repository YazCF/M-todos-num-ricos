import numpy as np
import matplotlib.pyplot as plt

# EDO
def f(x, T):
    return -0.25 * (T - 25)

# RK4
def runge_kutta_4(f, x0, y0, x_end, h):

    x_vals = [x0]
    y_vals = [y0]

    x, y = x0, y0

    # Tabla
    print("\nTABLA DE RESULTADOS - EJERCICIO 1")
    encabezados = ["x", "T"]
    header = " | ".join(f"{col:^12}" for col in encabezados)
    print(header)
    print("-" * len(header))

    print(" | ".join(f"{v:^12.6f}" for v in [x, y]))

    while x < x_end:
        k1 = f(x, y)
        k2 = f(x + h/2, y + h/2 * k1)
        k3 = f(x + h/2, y + h/2 * k2)
        k4 = f(x + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        x = x + h

        x_vals.append(x)
        y_vals.append(y)

        print(" | ".join(f"{v:^12.6f}" for v in [x, y]))

    return x_vals, y_vals

# Parámetros
x_vals, y_vals = runge_kutta_4(f, 0, 100, 2, 0.1)

# 🔥 SOLUCIÓN EXACTA
x_exact = np.linspace(0, 2, 100)
T_exact = 25 + 75 * np.exp(-0.25 * x_exact)

# 🔥 CREAR GRÁFICA (ESTO ERA LO IMPORTANTE)
plt.figure(figsize=(8,5))

plt.plot(x_vals, y_vals, 'bo-', label="RK4")
plt.plot(x_exact, T_exact, 'r--', label="Exacta")

plt.xlabel("x")
plt.ylabel("Temperatura (°C)")
plt.title("Transferencia de calor")

plt.legend()
plt.grid()

# ✅ GUARDAR BEFORE SHOW (MUY IMPORTANTE)
plt.savefig("ejercicio1_temperatura.png")

# ✅ MOSTRAR
plt.show()
