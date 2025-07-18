#ORDENAMIENTO BURBUJA

"""Ordenamiento burbuja de menor a mayor"""
def buble_sort_menor(lista):
    longitud_lista = len(lista)
    for i in range(longitud_lista - 1):
        hubo_cambio = False
        for j in range(longitud_lista - 1 - i):
            if lista[j] > lista[j + 1]:
                #Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return lista

"""Ordenamiento burbuja de mayor a menor"""
def buble_sort_mayor(lista):
    longitud_lista = len(lista)
    for i in range(longitud_lista - 1):
        hubo_cambio = False
        for j in range(longitud_lista - 1 - i):
            if lista[j] < lista[j + 1]:
                #Intercambio
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
                hubo_cambio = True
        if not hubo_cambio:
            break
    return lista
#Main
if __name__ == "__main__":
    numeros = [6, 3, 8 ,2, 5]
    print("Antes: ", numeros)
    buble_sort_menor(numeros)
    print("Despues: ", numeros)

if __name__ == "__main__":
    numeros = [6, 3, 8 ,2, 5]
    print("Antes: ", numeros)
    buble_sort_mayor(numeros)
    print("Despues: ", numeros)