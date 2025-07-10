def imprimir_lista(lista):
    print("\nLista de comidas favoritas:")
    for i, comida in enumerate(lista):
        print(f"{i + 1}. {comida}")
    print()

def modificar_lista(lista):
    imprimir_lista(lista)
    try:
        indice = int(input("¿Qué número de comida deseas modificar? (1, 2, 3...): ")) - 1
        if 0 <= indice < len(lista):
            nuevo_valor = input("¿Cuál es la nueva comida favorita?: ")
            lista[indice] = nuevo_valor
            print("¡Comida actualizada con éxito!")
        else:
            print("❌ Índice fuera de rango.")
    except ValueError:
        print("❌ Por favor, ingresa un número válido.")
