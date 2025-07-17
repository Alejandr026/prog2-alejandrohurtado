from encontrarMayor import encontrar_mayor
from sumarElementos import sumar_elementos

print("Probando encontrar mayor")
assert encontrar_mayor([1, 9, 1 ,8, 3, 7]) == 9
assert encontrar_mayor([-1, -9, -2, -8]) == -1
assert encontrar_mayor([42, 42, 42]) == 42
assert encontrar_mayor([]) == None # Prueb-----------------------------------------------------------------------------------a del caso especial
assert encontrar_mayor([5]) == 5
print("¡Pruebas para encontrar_mayor pasaron! ✅")

# Casos de Prueba con assert
print("\nProbando sumar_elementos...")
assert sumar_elementos([1, 2, 3, 4, 5]) == 15
assert sumar_elementos([10, -2, 5]) == 13
assert sumar_elementos([]) == 0 # ¡Importante probar con una lista vacía!
assert sumar_elementos([100]) == 100
print("¡Pruebas para sumar_elementos pasaron! ✅")