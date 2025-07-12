# busqueda.py
# 1. Definir la función busqueda_lineal
def busqueda_lineal(lista, clave):
    for i in range(len(lista)):
        if lista[i] == clave:
            return i
    return -1

# 3. Prueba tu función con assert
mi_lista_desordenada = [10, 5, 42, 8, 17, 30, 25]
print("Probando busqueda_lineal...")

assert busqueda_lineal(mi_lista_desordenada, 42) == 2
assert busqueda_lineal(mi_lista_desordenada, 10) == 0  # Al inicio
assert busqueda_lineal(mi_lista_desordenada, 25) == 6  # Al final
assert busqueda_lineal(mi_lista_desordenada, 99) == -1  # No existe
assert busqueda_lineal([], 5) == -1  # Lista vacía

print("¡Pruebas para busqueda_lineal pasaron! ✅")
print("JIMMY REQUENA - FIN DEL PROGRAMA")

# clase06_busquedas.py (continuación)
# 2. Definir la función busqueda_binaria
def busqueda_binaria(lista_ordenada, clave):
    izquierda = 0
    derecha = len(lista_ordenada) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista_ordenada[medio] == clave:
            return medio
        elif clave > lista_ordenada[medio]:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return -1

# 3. Prueba de la función
lista_ordenada = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
print("\nProbando busqueda_binaria...")

assert busqueda_binaria(lista_ordenada, 23) == 5
assert busqueda_binaria(lista_ordenada, 91) == 9  # Último
assert busqueda_binaria(lista_ordenada, 2) == 0   # Primero
assert busqueda_binaria(lista_ordenada, 3) == -1  # No existe
assert busqueda_binaria(lista_ordenada, 100) == -1  # Fuera de rango (mayor)

print("¡Pruebas para busqueda_binaria pasaron! ✅")
print("JIMMY REQUENA - FIN DEL PROGRAMA")


# clase06_busquedas.py (continuación)
print("\nRealizando el experimento del caos...")

# Lista desordenada del primer ejercicio
mi_lista_desordenada = [10, 8, 42, 5, 17, 30, 25]

# Buscamos un valor que sí está en la lista
resultado_caos = busqueda_binaria(mi_lista_desordenada, 30)

print(f"Búsqueda binaria de '30' en lista desordenada devolvió: {resultado_caos}")
# Probablemente devuelva -1 (fallo), o un índice incorrecto

print("JIMMY REQUENA - FIN DEL PROGRAMA")
