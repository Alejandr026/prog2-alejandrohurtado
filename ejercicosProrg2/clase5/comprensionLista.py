def es_matriz_simetrica(matriz):
    n = len(matriz)

    for fila in matriz:
        if len(fila) != n:
            return False
        
    for i in range(n):
        for j in range(i, n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def es_matriz_simetrica2(matriz):
    n = len(matriz)

    if any(len(fila) != n for fila in matriz):
        return False
    
    return all(matriz[i][j] == matriz[j][i] for i in range (n) for j in range (i, n))

