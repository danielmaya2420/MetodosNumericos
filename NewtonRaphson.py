import numpy as np
import matplotlib.pyplot as plt

def funcion(x):
    # Define aquí tu función
    return x**2 - 4

def derivada(x):
    # Define aquí la derivada de tu función
    return 2*x

def newton_raphson(x0, tolerancia, iter_max):
    """
    Función que implementa el método de Newton-Raphson para encontrar la raíz de una función.

    Args:
    x0 (float): Aproximación inicial.
    tolerancia (float): Tolerancia para el criterio de parada.
    iter_max (int): Número máximo de iteraciones.

    Returns:
    float: Aproximación de la raíz.
    """

    iteracion = 0
    while True:
        x1 = x0 - funcion(x0) / derivada(x0)
        iteracion += 1
        if abs(x1 - x0) < tolerancia or iteracion >= iter_max:
            break
        x0 = x1

    return x1

# Solicitar al usuario los valores iniciales
x0 = float(input("Ingrese la aproximación inicial: "))
tolerancia = float(input("Ingrese la tolerancia: "))
iter_max = int(input("Ingrese el número máximo de iteraciones: "))

# Llamar a la función de Newton-Raphson
raiz = newton_raphson(x0, tolerancia, iter_max)
print("La raíz encontrada es:", raiz)

# Graficar el método de Newton-Raphson
x_vals = np.linspace(x0 - 2, x0 + 2, 100)
y_vals = funcion(x_vals)

plt.plot(x_vals, y_vals, label='Función')
plt.scatter(raiz, funcion(raiz), color='red', label='Raíz')
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(raiz, color='black', linestyle='--', linewidth=0.5)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Método de Newton-Raphson')
plt.legend()
plt.grid(True)
plt.show()