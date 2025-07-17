# Solución al desafío adicional

# Función que suma los elementos de la diagonal secundaria de una matriz cuadrada
def sumar_diagonal_secundaria(matriz):
    """
    Recibe una matriz cuadrada (misma cantidad de filas y columnas)
    y devuelve la suma de los elementos en la diagonal secundaria.
    
    La diagonal secundaria va desde la esquina superior derecha
    hasta la esquina inferior izquierda.
    
    Por ejemplo, en una matriz 3x3:
        [[a, b, c],
         [d, e, f],
         [g, h, i]]
         
    La diagonal secundaria está en las posiciones: (0,2), (1,1), (2,0)
    y su suma sería: c + e + g
    """
    n = len(matriz)  # Número de filas (y columnas, ya que es cuadrada)
    suma = 0
    for i in range(n):
        suma += matriz[i][n - 1 - i]  # Accede al elemento en la posición (i, n-1-i)
    return suma


# Función de pruebas para validar que sumar_diagonal_secundaria funciona correctamente
def probar_suma_diagonal_secundaria():
    print("\nProbando sumar_diagonal_secundaria...")
    
    # Caso 1: matriz 3x3 normal
    m1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    resultado1 = sumar_diagonal_secundaria(m1)
    print(f"Matriz: {m1}")
    print(f"Suma esperada: 3 + 5 + 7 = 15")
    print(f"Suma obtenida: {resultado1}")
    
# Llamada a la función de prueba
probar_suma_diagonal_secundaria()
