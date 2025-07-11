# Definición de la función usando un for
def factorial(n):
    if n < 0:
        raise ValueError("❌ El factorial no está definido para números negativos.")

    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado


# Solicita un número al usuario
try:
    numero = int(input("Ingrese un número entero para calcular su factorial: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError as e:
    print(e)
