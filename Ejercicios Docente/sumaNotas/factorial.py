# Definición de la función recursiva
def factorial(n):
    if n < 0:
        raise ValueError("❌ El factorial no está definido para números negativos.")
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

assert factorial(0) == 1
assert factorial(1) == 1
assert factorial(5) == 120
assert factorial(6) == 720
print("¡Pruebas de factoriales pasaron! ✅")

# Solicita un número al usuario
try:
    numero = int(input("Ingrese un número entero para calcular su factorial: "))
    resultado = factorial(numero)
    print(f"El factorial de {numero} es: {resultado}")
except ValueError as e:
    print(e)
