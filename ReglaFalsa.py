import numpy as np
import matplotlib.pyplot as plt
import math

def funcion(x):
    # Define tu función aquí
    return math.sin(x) - x/2

def regla_falsa(func, a, b, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        fa = func(a)
        fb = func(b)

        # Nueva aproximación usando la regla falsa
        x1 = a - (fa * (b - a)) / (fb - fa)
        fx1 = func(x1)

        # Actualizar el intervalo
        if fx1 * fa > 0:
            a = x1
        else:
            b = x1

        # Verificar la convergencia
        if abs(fx1) < tol:
            break

    return x1

# Solicitar entrada del usuario
try:
    # Ingresar la función como una cadena (por ejemplo, "x**3 - 6*x**2 + 11*x - 6")
    expresion_funcion = input("Ingrese la función (en términos de 'x'): ")
    funcion = lambda x: eval(expresion_funcion)

    a = float(input("Ingrese el extremo izquierdo del intervalo (a): "))
    b = float(input("Ingrese el extremo derecho del intervalo (b): "))
    tolerancia = float(input("Ingrese la tolerancia: "))

    # Llamar a la función regla_falsa para encontrar la raíz
    raiz = regla_falsa(funcion, a, b, tol=tolerancia)

    print(f"La raíz aproximada es: {raiz}")

    # Graficar la función y la raíz encontrada
    x_vals = np.linspace(a, b, 400)
    y_vals = funcion(x_vals)
    plt.plot(x_vals, y_vals, label='Función')
    plt.scatter(raiz, funcion(raiz), color='red', label='Raíz')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(raiz, color='black', linestyle='--', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Gráfico de la función y la raíz encontrada')
    plt.legend()
    plt.grid(True)
    plt.show()

except (ValueError, SyntaxError):
    print("Error: Ingrese valores numéricos y una expresión de función válida.")