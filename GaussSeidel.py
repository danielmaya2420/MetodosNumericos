import numpy as np
import matplotlib.pyplot as plt

def gauss_seidel(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(A)
    x = x0[:]
    iter_count = 0

    errors = []  # Lista para almacenar los errores en cada iteración

    while iter_count < max_iter:
        x_new = x[:]
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x_new[j]
            x_new[i] = (b[i] - sigma) / A[i][i]
        if all(abs(x_new[i] - x[i]) < tol for i in range(n)):
            return x_new, iter_count, errors
        errors.append(np.linalg.norm(np.array(x_new) - np.array(x)))  # Agregar el error de esta iteración a la lista
        x = x_new[:]
        iter_count += 1
    raise ValueError("Gauss-Seidel method did not converge within maximum iterations")

if __name__ == "__main__":
    # Ingresar los valores de la matriz A y el vector b
    print("Ingrese la matriz A (una fila a la vez, separando los elementos por espacios):")
    A = []
    for _ in range(int(input("Número de filas de A: "))):
        A.append(list(map(float, input().split())))

    print("Ingrese el vector b (separando los elementos por espacios):")
    b = list(map(float, input().split()))

    # Ingresar el valor inicial de x
    print("Ingrese el valor inicial de x (separando los elementos por espacios):")
    x0 = list(map(float, input().split()))

    # Llamar a la función gauss_seidel
    try:
        solucion, iteraciones, errores = gauss_seidel(A, b, x0)
        print("La solución es:", solucion)
        # Graficar el error en función del número de iteraciones
        plt.plot(range(1, iteraciones + 1), errores, marker='o')
        plt.xlabel('Número de iteraciones')
        plt.ylabel('Error')
        plt.title('Convergencia del método de Gauss-Seidel')
        plt.grid(True)
        plt.show()
    except ValueError as e:
        print(e)