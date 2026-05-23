import numpy as np
import matplotlib.pyplot as plt

# Parámetros
V = 10
R = 1000
C = 0.001

# EDO
def f(t, q):
    return (V - q/C) / R

# Runge-Kutta 4
def runge_kutta_4(f, t0, q0, t_end, h):

    t_vals = [t0]
    q_vals = [q0]

    t, q = t0, q0

    # Tabla uniforme
    print("\nTABLA DE RESULTADOS - EJERCICIO 2")
    encabezados = ["t", "q"]
    header = " | ".join(f"{h:^12}" for h in encabezados)
    print(header)
    print("-" * len(header))

    print(" | ".join(f"{v:^12.6f}" for v in [t, q]))

    while t < t_end:
        k1 = f(t, q)
        k2 = f(t + h/2, q + h/2 * k1)
        k3 = f(t + h/2, q + h/2 * k2)
        k4 = f(t + h, q + h * k3)

        q = q + (h / 6) * (k1 + 2*k2 + 2*k3 + k4)
        t = t + h

        t_vals.append(t)
        q_vals.append(q)

        print(" | ".join(f"{v:^12.6f}" for v in [t, q]))

    return t_vals, q_vals

# Ejecutar
t_vals, q_vals = runge_kutta_4(f, 0, 0, 1, 0.05)

# Gráfica
plt.figure(figsize=(8,5))
plt.plot(t_vals, q_vals, 'bo-')

plt.xlabel("t")
plt.ylabel("Carga q(t)")
plt.title("Carga de un capacitor (RK4)")
plt.grid()

# Guardar automáticamente
plt.savefig("ejercicio2_carga.png")

plt.show()