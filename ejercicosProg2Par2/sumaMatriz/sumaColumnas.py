ventas = [
    [10, 10, 10, 10],  # Producto 1
    [10, 10, 10, 10],  # Producto 2
    [10, 10, 10, 10]   # Producto 3
]

suma_total = 0
num_columnas = len(ventas[0])

for j in range(num_columnas):  # Recorrer columnas
    suma_columna = 0
    for i in range(len(ventas)):  # Recorrer filas por cada columna
        suma_columna += ventas[i][j]
    print(f"Sumatoria de la columna {j} es: {suma_columna}")
    suma_total += suma_columna

print("La suma total de todo es: ", suma_total)
