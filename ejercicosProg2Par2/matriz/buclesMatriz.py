#Op 1: Recorriendo indices
matriz = [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ]
num_filas = len(matriz)
num_columnas = len(matriz[0])

for i in range(num_filas):
    for j in range(num_columnas):
        elemento = matriz[i][j]
        """
        Esto significa:

    matriz[1] da [4, 5, 6] (segunda fila)

    matriz[1][2] da 6 (el tercer elemento de esa fila)
        """
        print(f"Elemento en ({i}, {j}) es {elemento}")


for fila_actu in matriz:
    for elemento in fila_actu:
        print(elemento, end=" ")
    print()



