# Error relativo
def error_relativo(valor_verdadero, valor_aproximado):
    """
    Calcula el error relativo entre un valor verdadero y uno aproximado.

    Args:
    - valor_verdadero (float): El valor verdadero.
    - valor_aproximado (float): El valor aproximado.

    Returns:
    - error_relativo (float): El error relativo calculado.
    """
    return abs((valor_verdadero - valor_aproximado) / valor_verdadero)

def main():
    try:
        valor_verdadero = float(input("Ingrese el valor verdadero: "))
        valor_aproximado = float(input("Ingrese el valor aproximado: "))

        error_rel = error_relativo(valor_verdadero, valor_aproximado)
        print("El error relativo es:", error_rel)

    except ValueError:
        print("Error: ¡Ingrese números válidos!")

if __name__ == "__main__":
    main()