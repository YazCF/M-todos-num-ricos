import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

R = 1000
C = 0.001
Vf = 5

def f(t, V):
    return (1/(R*C)) * (Vf - V)

t0 = 0
V0 = 0
tf = 5
n = 20

h = (tf - t0) / n

t_vals = [t0]
V_vals = [V0]

t = t0
V = V0

for i in range(n):
    V = V + h * f(t, V)
    t = t + h
    t_vals.append(t)
    V_vals.append(V)

t_exact = np.linspace(0, 5, 100)
V_exact = Vf * (1 - np.exp(-t_exact/(R*C)))

df = pd.DataFrame({"t": t_vals, "V_aprox": V_vals})
df.to_csv("ej1_capacitor.csv", index=False)

plt.figure()
plt.plot(t_vals, V_vals, 'o-', label='Euler')
plt.plot(t_exact, V_exact, label='Exacta')
plt.title("Carga de un capacitor (RC)")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje (V)")
plt.legend()
plt.grid()

plt.savefig("ej1_capacitor.png")  # GUARDAR
plt.show()