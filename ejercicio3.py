#   Codigo que implementa el calculo de errores
#   en operaciones numericas
# 
#           Autor:
#   Dr. Ivan de Jesus May-Cen
#   imaycen@hotmail.com
#   Version 1.0 : 29/01/2025
#

def calcular_errores(x, y, valor_real):
    diferencia = x - y

    error_abs = abs(valor_real - diferencia)
    error_rel = error_abs / abs(valor_real)
    error_pct = error_rel * 100

    print(f"Diferencia calculada (x - y): {diferencia:.20e}")
    print(f"Valor exacto esperado: {valor_real:.20e}")
    print(f"Error absoluto: {error_abs:.20e}")
    print(f"Error relativo: {error_rel:.20e}")
    print(f"Error porcentual: {error_pct:.12f}%")
    return error_abs, error_rel

valores = [(1.0000001, 1.0000000, 0.0000001), (1.000000000000001, 1.000000000000000, 0.000000000000001)]

for x, y, real in valores:
    print(f"\nPara x={x}, y={y}:")
    calcular_errores(x, y, real)