# Definición de la función
def invertir_lista(lista_original):
    lista_invertida = []

    # Recorremos la lista desde el final hasta el inicio
    for i in range(len(lista_original) - 1, -1, -1):
        lista_invertida.append(lista_original[i])

    return lista_invertida

# -------------------------
# 🧪 Casos de prueba con assert
# -------------------------

print("\nProbando invertir_lista...")

lista_prueba = [1, 2, 3, 4, 5]
lista_resultante = invertir_lista(lista_prueba)

assert lista_resultante == [5, 4, 3, 2, 1], "❌ Error en inversión"
assert lista_prueba == [1, 2, 3, 4, 5], "❌ ¡La lista original fue modificada!"
assert invertir_lista(["a", "b", "c"]) == ["c", "b", "a"]
assert invertir_lista([]) == []

print("¡Pruebas para invertir_lista pasaron! ✅")
