def contar_elemento(lista, elemento_buscado):
    return lista.count(elemento_buscado)
print("\nProbando contar_elemento con .count()...")

assert contar_elemento([1, 2, 3, 2, 4, 2], 2) == 3
assert contar_elemento([1, 2, 3, 2, 4, 2],1) == 1
assert contar_elemento(["a", "b", "a", "c", "a"], "a") == 3
assert contar_elemento(["sol", "luna", "estrella"], "marte") == 0
assert contar_elemento([], 5) == 0
assert contar_elemento([True, False, True, True], True) == 3

print("¡Pruebas con .count() pasaron! ✅")
