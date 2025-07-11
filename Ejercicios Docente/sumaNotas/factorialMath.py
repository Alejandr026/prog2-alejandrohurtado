import math

def factorial(n):
    if n < 0:
        raise ValueError("❌ El factorial no está definido para números negativos.")
    return 1 if n == 0 else math.prod(range(1, n + 1))

def mostrar_factorial(n):
    if n < 0:
        print("❌ El factorial no está definido para números negativos.")
        return

    pasos = ' x '.join(str(i) for i in range(1, n + 1)) if n > 0 else "1"
    resultado = factorial(n)
    print(f"{pasos} = {resultado}")

# -------------------
# Ejecución interactiva
# -------------------
try:
    numero = int(input("Ingrese un número entero para calcular su factorial: "))
    mostrar_factorial(numero)
except ValueError:
    print("❌ Entrada inválida. Por favor ingresa un número entero.")
