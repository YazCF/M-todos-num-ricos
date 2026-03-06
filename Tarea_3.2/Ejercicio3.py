import numpy as np
import matplotlib.pyplot as plt

def gauss_jordan_pivot_determinante(A, b):
   
    n = len(A)
    Ab = np.hstack([A, b.reshape(-1, 1)]).astype(float)
    det_A = np.linalg.det(A)
    
    if np.isclose(det_A, 0):
        mensaje = f"Determinante de A: {det_A:.5f}. El sistema es indeterminado o no tiene solución única."
        print(mensaje)
        return None
    
    mensaje = f"Determinante de A: {det_A:.5f}. El sistema tiene solución única."
    print(mensaje)

    soluciones_parciales = []
    
    for i in range(n):
        max_row = np.argmax(abs(Ab[i:, i])) + i
        if i != max_row:
            Ab[[i, max_row]] = Ab[[max_row, i]]

        Ab[i] = Ab[i] / Ab[i, i]

        for j in range(n):
            if i != j:
                Ab[j] -= Ab[j, i] * Ab[i]

        soluciones_parciales.append(Ab[:, -1].copy())

    x_final = soluciones_parciales[-1]
    errores = [np.linalg.norm(x - x_final) / np.linalg.norm(x_final) for x in soluciones_parciales]

    # Graficar el error relativo
    plt.figure()
    plt.semilogy(range(1, len(errores)+1), errores, marker='o', color='blue')
    plt.xlabel("Paso de eliminación")
    plt.ylabel("Error relativo")
    plt.title("Error relativo durante el proceso de Gauss-Jordan")
    plt.grid(True)
    plt.show()

    return x_final

# Definir el sistema de ecuaciones
A_test = np.array([[2, -3, 4, -1, 5, -1, 2, -1, 3, -2],
               [-3, 2, 5, -1, 4, 2, -3, 1, -2, 5],
               [4, -1, 3, 2, -3, 1, -2, 5, -4, 1],
               [-1, 5, -2, 3, 4, -1, 2, -3, 1, -5],
               [3, -2, 5, -1, 4, 2, -3, 1, -5, 2],
               [-2, 4, -3, 1, 5, -1, 2, -4, 3, -1],
               [5, -1, 2, -3, 4, 1, -2, 3, -1, 4],
               [1, -3, 4, -2, 5, -1, 2, -1, 4, -3],
               [2, 3, -1, 4, -2, 5, -3, 1, -2, 1],
               [-3, 2, 4, -1, 3, -2, 5, -1, 1, -4]
                   ], dtype=float)

b_test = np.array([11, -10, 8, -6, 7, -3, 9, -5, 6, -8], dtype=float)

# Resolver el sistema
solucion_test = gauss_jordan_pivot_determinante(A_test, b_test)

# Imprimir la solución si existe
if solucion_test is not None:
    print("Solución del sistema:", solucion_test)