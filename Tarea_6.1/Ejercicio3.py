import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

k = 0.07
Tamb = 25

def f(t, T):
    return -k * (T - Tamb)

t0 = 0
T0 = 90
tf = 30
n = 30

h = (tf - t0) / n

t_vals = [t0]
T_vals = [T0]

t = t0
T = T0

for i in range(n):
    T = T + h * f(t, T)
    t = t + h
    t_vals.append(t)
    T_vals.append(T)

t_exact = np.linspace(0, 30, 100)
T_exact = Tamb + (T0 - Tamb) * np.exp(-k*t_exact)

df = pd.DataFrame({"t": t_vals, "T_aprox": T_vals})
df.to_csv("ej3_enfriamiento.csv", index=False)

plt.figure()
plt.plot(t_vals, T_vals, 'o-', label='Euler')
plt.plot(t_exact, T_exact, label='Exacta')
plt.title("Enfriamiento de Newton")
plt.xlabel("Tiempo (min)")
plt.ylabel("Temperatura (°C)")
plt.legend()
plt.grid()

plt.savefig("ej3_enfriamiento.png")  # GUARDAR
plt.show()