def merge_sort(lista):
    # Paso Vencer (Condición Base de la Recursividad):
    # Si la lista tiene 1 elemento o menos, ¡ya está ordenada!
    if len(lista) <= 1:
        return lista

    # Paso 1: DIVIDIR
    medio = len(lista) // 2
    mitad_izquierda = lista[:medio]     # Slicing para obtener la primera mitad
    mitad_derecha = lista[medio:]       # Slicing para la segunda mitad

    # Paso 2: VENCER (Recursión)
    izquierda_ordenada = merge_sort(mitad_izquierda)
    derecha_ordenada = merge_sort(mitad_derecha)

    # Paso 3: COMBINAR
    resultado = merge(izquierda_ordenada, derecha_ordenada)
    return resultado


# --- Función de Mezcla (merge) ---
def merge(izquierda, derecha):
    resultado = []
    i = 0
    j = 0

    # Comparar elementos de ambas mitades
    while i < len(izquierda) and j < len(derecha):
        if izquierda[i] <= derecha[j]:  # Menor a mayor
            resultado.append(izquierda[i])
            i += 1
        else:
            resultado.append(derecha[j])
            j += 1

    # Agregar elementos restantes si alguna lista no terminó
    resultado.extend(izquierda[i:])
    resultado.extend(derecha[j:])

    return resultado


# --- Prueba ---
if __name__ == "__main__":
    numeros = [6, 3, 8, 2, 5]
    print("Antes: ", numeros)
    ordenados = merge_sort(numeros)
    print("Después (menor a mayor):", ordenados)
