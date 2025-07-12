

def merge_sort(lista):
  # Paso Vencer (Condición Base de la Recursividad):
  if len(lista) <= 1:
      return lista

  # Paso 1: DIVIDIR
  medio = len(lista) // 2
  mitad_izquierda = lista[:medio]
  mitad_derecha = lista[medio:]

  # Paso 2: VENCER (Recursión)
  izquierda_ordenada = merge_sort(mitad_izquierda)
  derecha_ordenada = merge_sort(mitad_derecha)

  # Paso 3: COMBINAR
  print(f"Mezclaría {izquierda_ordenada} y {derecha_ordenada}")
  return merge(izquierda_ordenada, derecha_ordenada)

def merge(izquierda, derecha):
  resultado = []
  i = j = 0

  # Comparar elementos de izquierda y derecha uno por uno
  while i < len(izquierda) and j < len(derecha):
      if izquierda[i] < derecha[j]:
          resultado.append(izquierda[i])
          i += 1
      else:
          resultado.append(derecha[j])
          j += 1

  # Agregar cualquier elemento restante
  resultado.extend(izquierda[i:])
  resultado.extend(derecha[j:])

  return resultado

# --- Prueba ---
lista_prueba = [8, 3, 5, 1]
print("Lista original:", lista_prueba)
resultado = merge_sort(lista_prueba)
print("Lista ordenada:", resultado)

# --- Pruebas automatizadas ---
assert merge_sort([]) == []                         # Lista vacía
assert merge_sort([1]) == [1]                       # Lista con un solo elemento
assert merge_sort([5, 2]) == [2, 5]                  # Lista con dos elementos
assert merge_sort([3, 1, 2]) == [1, 2, 3]            # Lista con tres elementos desordenados
assert merge_sort([10, 5, 3, 8, 6, 2]) == [2, 3, 5, 6, 8, 10]  # Lista par
assert merge_sort([9, 7, 5, 3, 1]) == [1, 3, 5, 7, 9]  # Lista en orden descendente
assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]  # Lista ya ordenada
assert merge_sort([4, 2, 2, 4, 1]) == [1, 2, 2, 4, 4]  # Lista con elementos repetidos
assert merge_sort([100, -50, 0, 50, -100]) == [-100, -50, 0, 50, 100]  # Lista con enteros negativos y positivos
assert merge_sort([2.5, 1.2, 3.8]) == [1.2, 2.5, 3.8]  # Lista con flotantes
print("¡Todas las pruebas con assert pasaron correctamente!")

print("JIM REQUENA - FIN DEL PROGRAMA")