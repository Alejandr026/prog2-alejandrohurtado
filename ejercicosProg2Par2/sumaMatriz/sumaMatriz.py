
ventas = [
[10, 10, 10, 10], # Producto 1 en Sucursales A, B, C, D
[10, 10, 10, 10], # Producto 2 ...
[10, 10, 10, 10] # Producto 3 ...
]

print(f"El numero mayor de la lista es:  ")

acumulador_total = 0
for i in range(len(ventas)):
    for j in range(len(ventas[i])):
        acumulador_total += ventas[i][j]

print("Suma total: ", acumulador_total)




