import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

g = 9.81
m = 2
k = 0.5

def f(t, v):
    return g - (k/m)*v

t0 = 0
v0 = 0
tf = 10
n = 50

h = (tf - t0) / n

t_vals = [t0]
v_vals = [v0]

t = t0
v = v0

for i in range(n):
    v = v + h * f(t, v)
    t = t + h
    t_vals.append(t)
    v_vals.append(v)

t_exact = np.linspace(0, 10, 100)
v_exact = (m*g/k)*(1 - np.exp(-k*t_exact/m))

df = pd.DataFrame({"t": t_vals, "v_aprox": v_vals})
df.to_csv("ej2_caida.csv", index=False)

plt.figure()
plt.plot(t_vals, v_vals, 'o-', label='Euler')
plt.plot(t_exact, v_exact, label='Exacta')
plt.title("Caída libre con resistencia del aire")
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.legend()
plt.grid()

plt.savefig("ej2_caida.png")  # GUARDAR
plt.show()