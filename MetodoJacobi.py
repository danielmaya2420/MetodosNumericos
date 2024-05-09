import numpy as np
import matplotlib.pyplot as plt

def jacobi(A, b, x0, tol=1e-6, max_iter=1000):
    n = len(b)
    x = np.copy(x0)
    x_new = np.zeros_like(x)
    iteration = 0
    error = tol + 1

    errors = []  # Lista para almacenar los errores en cada iteración

    while error > tol and iteration < max_iter:
        for i in range(n):
            sigma = 0
            for j in range(n):
                if j != i:
                    sigma += A[i][j] * x[j]
            x_new[i] = (b[i] - sigma) / A[i][i]

        error = np.linalg.norm(x_new - x)
        errors.append(error)  # Agregar el error de esta iteración a la lista
        x = np.copy(x_new)
        iteration += 1

    return x, iteration, errors

def main():
    n = int(input("Ingrese el número de ecuaciones del sistema: "))
    A = []
    b = []
    print("Ingrese los coeficientes de la matriz A:")
    for i in range(n):
        row = list(map(float, input().split()))
        A.append(row)
    print("Ingrese los términos constantes del sistema:")
    b = list(map(float, input().split()))
    x0 = np.zeros(n)  # Asumiendo una aproximación inicial de ceros

    solution, iterations, errors = jacobi(A, b, x0)
    print("\nLa solución aproximada es:")
    for i in range(n):
        print("x{} = {:.6f}".format(i+1, solution[i]))
    print("\nNúmero de iteraciones realizadas:", iterations)

    # Graficar el error en función del número de iteraciones
    plt.plot(range(1, iterations + 1), errors, marker='o')
    plt.xlabel('Número de iteraciones')
    plt.ylabel('Error')
    plt.title('Convergencia del método de Jacobi')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()