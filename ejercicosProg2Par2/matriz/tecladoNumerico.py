from funcionesMatriz import imprimir_matriz_pythonico

teclado = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
"""fUNCION PARA IMPRIMIR EN PYTHONICO"""
imprimir_matriz_pythonico(teclado)
print()

for fila_actual in teclado:
    for elemento in fila_actual:
        print(elemento, end=" ")
    print()

