#Error relativo porcentual
def calcular_error_relativo_porcentual(valor_exacto, valor_aproximado):
    """
    Calcula el error relativo porcentual dado un valor exacto y un valor aproximado.

    Args:
    - valor_exacto: El valor exacto o teórico.
    - valor_aproximado: El valor obtenido mediante algún método numérico.

    Returns:
    - El error relativo porcentual.
    """
    error_absoluto = abs(valor_exacto - valor_aproximado)
    error_relativo_porcentual = (error_absoluto / abs(valor_exacto)) * 100
    return error_relativo_porcentual

# Solicitar al usuario que ingrese los valores
valor_exacto = float(input("Ingrese el valor exacto: "))
valor_aproximado = float(input("Ingrese el valor aproximado: "))

# Calcular el error relativo porcentual
error_rel_porcentual = calcular_error_relativo_porcentual(valor_exacto, valor_aproximado)

# Mostrar el resultado
print("El error relativo porcentual es:", error_rel_porcentual, "%")