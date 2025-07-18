def imprimir_matriz_pythonico (matriz):
    for fila_actu in matriz:
        for elemento in fila_actu:
            print(elemento, end=" ")
        print()
        
def imprimir_matriz(matriz):        
    num_filas = len(matriz)
    num_columnas = len(matriz[0])
    for i in range(num_filas):
        for j in range(num_columnas):
            elemento = matriz[i][j]
            print(f"Elemento en ({i}, {j}) es {elemento}")