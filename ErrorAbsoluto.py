#Error absoluto
def calcular_error_absoluto(valor_exacto, valor_aproximado):
    """
    Calcula el error absoluto dado un valor exacto y un valor aproximado.

    Args:
    - valor_exacto: El valor exacto o teórico.
    - valor_aproximado: El valor obtenido mediante algún método numérico.

    Returns:
    - El error absoluto.
    """
    error_absoluto = abs(valor_exacto - valor_aproximado)
    return error_absoluto

# Solicitar al usuario que ingrese los valores
valor_exacto = float(input("Ingrese el valor exacto: "))
valor_aproximado = float(input("Ingrese el valor aproximado: "))

# Calcular el error absoluto
error = calcular_error_absoluto(valor_exacto, valor_aproximado)

# Mostrar el resultado
print("El error absoluto es:", error)