#   Codigo que implementa un esquema numerico 
#   para determinar la aproximacion de Leibniz
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#

import numpy as np
import matplotlib.pyplot as plt

def leibniz_pi(n):
    return 4 * sum((-1)**k / (2*k + 1) for k in range(n))

true_pi = 3.141592653589793
N_values = [10, 100, 1000, 10000]

errors_abs = []
errors_rel = []
errors_sq=[]

print(f"{'N':>8} | {'pi_aprox':>15} | {'err_abs':>15} | {'err_rel':>15} | {'err_cuad':>15}")
print("-" * 80)

for N in N_values:
    approx_pi = leibniz_pi(N)
    error_abs = abs(true_pi - approx_pi)
    error_rel = error_abs / true_pi
    error_cuad = error_abs**2
    errors_abs.append(error_abs)
    errors_rel.append(error_rel)
    errors_sq.append(error_cuad)
    print(f"{N:8d} | {approx_pi:15.12f} | {error_abs:15.6e} | {error_rel:15.6e} | {error_cuad:15.6e}")

plt.figure()
plt.plot(N_values, errors_abs, label='Error absoluto', marker='o')
plt.plot(N_values, errors_rel, label='Error relativo', marker='s')
plt.xscale('log')
plt.yscale('log')
plt.xlabel('N')
plt.ylabel('Error')
plt.legend()
plt.title('Errores en la aproximación de pi')
plt.grid(True)
plt.show()