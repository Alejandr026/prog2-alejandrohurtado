# Definición de la función
def encontrar_mayor(lista_numeros):
    # Caso especial: lista vacía
    if not lista_numeros:
        return None

    # Paso 1: El primer "campeón"
    mayor_temporal = lista_numeros[0]

    # Paso 2-4: Recorrer la lista para buscar al más grande
    for elemento in lista_numeros:
        if elemento > mayor_temporal:
            mayor_temporal = elemento

    # Paso 5: Devolver el campeón
    return mayor_temporal

# -------------------------
# 🧪 Casos de prueba con assert
# -------------------------

print("Probando encontrar_mayor...")

assert encontrar_mayor([1, 5, 3, 9, 2]) == 9
assert encontrar_mayor([-10, -5, -3, -20]) == -3
assert encontrar_mayor([7, 7, 7, 7]) == 7
assert encontrar_mayor([]) == None  # lista vacía
assert encontrar_mayor([42]) == 42  # un solo elemento

print("¡Pruebas para encontrar_mayor pasaron! ✅")
