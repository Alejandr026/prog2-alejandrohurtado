def sumar_diagonal_secundaria (matriz):
    n = (len(matriz))
    suma = 0
    for i in range(n):
        suma += matriz[i][n - 1 - i]
    return suma

def probar_suma_diagonal_secundaria():
    print("\nProbando sumar_diagonal_secundaria...")
    # Caso 1: matriz 3x3 normal
    m1 = [[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    # Diagonal secundaria: 3 + 5 + 7 = 15
    assert sumar_diagonal_secundaria(m1) == 15
    # Caso 2: matriz 2x2
    m2 = [[10, 1],
    [2, 20]]
    # Diagonal secundaria: 1 + 2 = 3
    assert sumar_diagonal_secundaria(m2) == 3
    # Caso 3: matriz 1x1
    m3 = [[42]]
    # Solo hay un elemento: 42
    assert sumar_diagonal_secundaria(m3) == 42
    
    print("¡Pruebas para sumar_diagonal_secundaria pasaron! ✅")
    # Llamamos a la función de prueba
probar_suma_diagonal_secundaria()