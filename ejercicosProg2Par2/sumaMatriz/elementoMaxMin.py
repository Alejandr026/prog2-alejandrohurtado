lista = [
[10, 20, 30, 40], # Producto 1 en Sucursales A, B, C, D
[50, 60, 70, 80], # Producto 2 ...
[90, 100, 110, 120] # Producto 3 ...
]

mayor_temporal = lista[0][0]
for i in range(len(lista)):
    for j in range(len(lista[i])):
        if lista [i][j] > mayor_temporal:
            mayor_temporal = lista[i][j]

print(mayor_temporal)