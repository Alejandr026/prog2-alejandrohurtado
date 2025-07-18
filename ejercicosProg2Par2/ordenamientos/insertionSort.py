def insertion_sort_menor(lista):
    for i in range(1, len(lista)):
        valor_actu = lista[i]
        posicion_actu = i

        while posicion_actu > 0 and lista[posicion_actu - 1] > valor_actu:
            lista[posicion_actu] = lista[posicion_actu - 1]
            posicion_actu -= 1
        lista[posicion_actu] = valor_actu

    return lista

def insertion_sort_mayor (lista):
    for i in range(1, len(lista)):
        valor_actu = lista[i]
        posicion_actu = i

        while posicion_actu > 0 and lista[posicion_actu - 1] < valor_actu:
            lista[posicion_actu] = lista[posicion_actu - 1]
            posicion_actu -= 1
        lista[posicion_actu] = valor_actu

    return lista

if __name__ == "__main__":
    numeros = [6, 3, 8 ,2, 5]
    print("Antes: ", numeros)
    insertion_sort_mayor(numeros)
    print("Despues: ", numeros)