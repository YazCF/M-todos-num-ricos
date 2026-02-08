#   Codigo que implementa un esquema numerico 
#   para determinar la precision de una maquina
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#

import numpy as np
import pandas as pd

epsilon = 1.0
iteracion = 0
datos = []

while 1.0 + epsilon != 1.0:
    epsilon /= 2
    iteracion = iteracion + 1
    datos.append([iteracion, epsilon])
    print(f"Iteracion: {iteracion}, Precisión de máquina: {epsilon}")

epsilon *= 2
print(f"Precisión de máquina: {epsilon}")

df = pd.DataFrame(datos, columns=["Iteracion", "Epsilon"])
df.to_excel("Ejercicio1.xlsx", index=False)
print("Archivo excel generado: Ejercicio1.xlsx")