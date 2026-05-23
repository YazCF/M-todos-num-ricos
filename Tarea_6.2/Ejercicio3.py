import numpy as np
import matplotlib.pyplot as plt

# Sistema de ecuaciones
def f(t, y):
    y1, y2 = y
    dy1 = y2
    dy2 = -2*y2 - 5*y1
    return np.array([dy1, dy2])

# Runge-Kutta para sistema
def runge_kutta_4_system(f, t0, y0, t_end, h):

    t_vals = [t0]
    y_vals = [y0]

    t = t0
    y = np.array(y0)

    # Tabla uniforme
    print("\nTABLA DE RESULTADOS - EJERCICIO 3")
    encabezados = ["t", "y1", "y2"]
    header = " | ".join(f"{h:^12}" for h in encabezados)
    print(header)
    print("-" * len(header))

    print(" | ".join(f"{v:^12.6f}" for v in [t, y[0], y[1]]))

    while t < t_end:
        k1 = f(t, y)
        k2 = f(t + h/2, y + h/2 * k1)
        k3 = f(t + h/2, y + h/2 * k2)
        k4 = f(t + h, y + h * k3)

        y = y + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h

        t_vals.append(t)
        y_vals.append(y)

        print(" | ".join(f"{v:^12.6f}" for v in [t, y[0], y[1]]))

    return t_vals, np.array(y_vals)

# Ejecutar
t_vals, y_vals = runge_kutta_4_system(f, 0, [1, 0], 5, 0.1)

# Gráfica (posición)
plt.figure(figsize=(8,5))
plt.plot(t_vals, y_vals[:,0], 'bo-', label="Posición y(t)")

plt.xlabel("t")
plt.ylabel("y(t)")
plt.title("Sistema masa-resorte amortiguado")
plt.legend()
plt.grid()

# Guardar automáticamente
plt.savefig("ejercicio3_resorte.png")

plt.show()