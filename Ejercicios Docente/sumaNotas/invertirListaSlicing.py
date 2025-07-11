def invertir_lista(lista_original):
# lista[inicio:fin:paso]
    return lista_original[::-1]
# Esto usa slicing con paso negativo
# inicio: índice desde donde empezar (incluye este elemento).
# fin: índice hasta donde cortar (no incluye este elemento).
# paso: cuántos pasos avanzar (puede ser negativo).


# Pruebas
print("\nProbando invertir_lista con slicing...")

lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = invertir_lista(lista_prueba)

assert lista_resultante == [5, 4, 3, 2, 1], "❌ Error en inversión con slicing"
assert lista_prueba == [1, 2, 3, 4, 5], "❌ ¡La lista original fue modificada!"
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []

print("¡Pruebas con slicing pasaron! ✅")
