ventas = [
[10, 10, 10, 10], # Producto 1 en Sucursales A, B, C, D
[10, 10, 10, 10], # Producto 2 ...
[10, 10, 10, 10] # Producto 3 ...
]


suma_total = 0
for i in range(len(ventas)):
    suma_por_fila = 0
    for j in range(len(ventas[i])):
        suma_por_fila += ventas[i][j]
    print(f"Sumatoria de la fila {i} es: {suma_por_fila}")
    suma_total += suma_por_fila

print("La suma total de todo es: ", suma_total)