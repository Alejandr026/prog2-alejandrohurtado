def ordenamiento_burbuja(lista):
    """
    Ordena una lista en orden ascendente utilizando el algoritmo de burbuja.
    Modifica la lista original (in-place) y también la retorna por conveniencia.
    """
    n = len(lista)  # Cantidad de elementos en la lista

    for i in range(n - 1):  # Bucle exterior para las pasadas
        hubo_intercambio = False  # Marca si hubo un intercambio en esta pasada

        # Bucle interior para las comparaciones e intercambios
        for j in range(n - 1 - i):  # Cada pasada evita revisar los últimos ya ordenados
            if lista[j] > lista[j + 1]:
                # ¡Intercambio!
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_intercambio = True

        if not hubo_intercambio:  # Si no hubo ningún intercambio, la lista ya está ordenada
            break

    return lista  # Opcional: también se puede omitir


if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes:", numeros)
    ordenamiento_burbuja(numeros)
    print("Después Ordenamiento Burbuja:", numeros)

# ------------------------------------------------
# Pruebas usando assert algoritmo de burbuja
# ------------------------------------------------

# Caso 1: Lista desordenada
lista1 = [6, 3, 8, 2, 5]
ordenamiento_burbuja(lista1)
assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1"

# Caso 2: Lista ya ordenada
lista2 = [1, 2, 3, 4, 5]
ordenamiento_burbuja(lista2)
assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2"

# Caso 3: Lista ordenada a la inversa (peor caso)
lista3 = [5, 4, 3, 2, 1]
ordenamiento_burbuja(lista3)
assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3"

# Caso 4: Lista con elementos duplicados
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_burbuja(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4"

# Caso borde: Lista vacía
assert ordenamiento_burbuja([]) == [], "Fallo en lista vacía"

# Caso borde: Lista con un solo elemento
assert ordenamiento_burbuja([42]) == [42], "Fallo en lista con un solo elemento"

print("¡Todas las pruebas ordenamiento burbuja pasaron! ✅")
print("JIM REQUENA - FIN PROGRAMA ORDENAMIENTO BURBUJA")


def ordenamiento_insercion(lista):
    """
    Ordena la lista in-place (modificando la original) usando el algoritmo de inserción.
    Retorna la misma lista por conveniencia.
    """
    for i in range(1, len(lista)):
        valor_actual = lista[i]  # La "carta" que vamos a insertar
        posicion_actual = i

        # Desplazar elementos mayores hacia la derecha
        while posicion_actual > 0 and lista[posicion_actual - 1] > valor_actual:
            lista[posicion_actual] = lista[posicion_actual - 1]
            posicion_actual -= 1

        # Insertar la "carta" en su hueco correcto
        lista[posicion_actual] = valor_actual

    return lista


# ------------------------------------------------
# Pruebas usando assert algoritmo de inserción
# ------------------------------------------------

# Caso 1: Lista desordenada
lista1 = [6, 3, 8, 2, 5]
print("Antes:", lista1)
ordenamiento_insercion(lista1)
print("Después Ordenamiento Inserción:", lista1)
assert lista1 == [2, 3, 5, 6, 8], "Fallo en Caso 1"

# Caso 2: Lista ya ordenada
lista2 = [1, 2, 3, 4, 5]
print("Antes:", lista2)
ordenamiento_insercion(lista2)
print("Después Ordenamiento Inserción:", lista2)
assert lista2 == [1, 2, 3, 4, 5], "Fallo en Caso 2"

# Caso 3: Lista ordenada a la inversa (peor caso)
lista3 = [5, 4, 3, 2, 1]
ordenamiento_insercion(lista3)
assert lista3 == [1, 2, 3, 4, 5], "Fallo en Caso 3"

# Caso 4: Lista con duplicados
lista4 = [5, 1, 4, 2, 8, 5, 2]
ordenamiento_insercion(lista4)
assert lista4 == [1, 2, 2, 4, 5, 5, 8], "Fallo en Caso 4"

# Caso borde: Lista vacía
assert ordenamiento_insercion([]) == [], "Fallo en lista vacía"

# Caso borde: Lista con un solo elemento
assert ordenamiento_insercion([42]) == [42], "Fallo en lista con un solo elemento"

print("¡Todas las pruebas del ordenamiento por inserción pasaron! ✅")
print("JIM REQUENA - FIN PROGRAMA ORDENAMIENTO INSERCIÓN")