# Definición de la función
def contar_elemento(lista, elemento_buscado):
    contador = 0
    for elemento in lista:
        if elemento == elemento_buscado:
            contador += 1
    return contador

# -------------------------
# 🧪 Casos de prueba con assert
# -------------------------

print("\nProbando contar_elemento...")

assert contar_elemento([1, 2, 3, 2, 4, 2], 2) == 3
assert contar_elemento(["a", "b", "a", "c", "a"], "a") == 3
assert contar_elemento(["sol", "luna", "estrella"], "marte") == 0
assert contar_elemento([], 5) == 0
assert contar_elemento([True, False, True, True], True) == 3

print("¡Pruebas para contar_elemento pasaron! ✅")
