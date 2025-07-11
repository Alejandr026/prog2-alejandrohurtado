# Definición de la función para sumar elementos
def sumar_elementos(lista_numeros):
    acumulador_suma = 0
    for elemento_actual in lista_numeros:
        acumulador_suma += elemento_actual
    return acumulador_suma

# Casos de prueba con assert
print("Probando sumar_elementos...")

assert sumar_elementos([1, 2, 3, 4, 5]) == 15
assert sumar_elementos([10, -2, 5]) == 13
assert sumar_elementos([]) == 0  # ¡Importante probar con una lista vacía!
assert sumar_elementos([100]) == 100

print("OK! ¡Pruebas para sumar_elementos pasaron!")
