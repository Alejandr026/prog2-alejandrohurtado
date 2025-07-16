import math

def busqueda_binaria(lista, valor_a_buscar):
    izquierda = 0
    derecha = len(lista) - 1

    while izquierda <= derecha:
        medio = math.floor((izquierda + derecha) / 2)

        print(f"Iteración:")
        print(f"  Izquierda = {izquierda}, Derecha = {derecha}, Medio = {medio}")
        print(f"  lista[{medio}] = {lista[medio]}")

        if lista[medio] == valor_a_buscar:
            print(f"  ¡Encontrado! El valor {valor_a_buscar} está en el índice {medio}.")
            return medio
        elif valor_a_buscar > lista[medio]:
            print(f"  {valor_a_buscar} > {lista[medio]} → Buscamos en la mitad derecha")
            izquierda = medio + 1
        else:
            print(f"  {valor_a_buscar} < {lista[medio]} → Buscamos en la mitad izquierda")
            derecha = medio - 1
        print("-" * 50)

    print(f"El valor {valor_a_buscar} no se encuentra en la lista.")
    return None

# Lista ordenada de ejemplo
lista = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]

# Buscar un número que está
busqueda_binaria(lista, 23)

print("\n" + "=" * 50 + "\n")

# Buscar un número que no está
busqueda_binaria(lista, 80)
