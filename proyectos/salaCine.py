def crear_sala(filas, columnas):
    sala  = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            if 2 <= j <= 5:
                precio = 50
            else:
                precio = 30
            fila.append({"estado" : "L", "precio": precio})
        sala.append(fila)
    return sala