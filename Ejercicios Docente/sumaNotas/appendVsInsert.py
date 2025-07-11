# Creamos una lista vacía
numeros = []

# append agrega al final
numeros.append(10)
numeros.append(20)
print("Usando append:", numeros)  # [10, 20]

# insert agrega en una posición específica
numeros.insert(1, 15)  # insertar en índice 1 el valor 15
print("Usando insert:", numeros)  # [10, 15, 20]


# Queremos duplicar cada número
numeros = [1, 2, 3, 4]
duplicados = list(map(lambda x: x * 5.5, numeros))
print("Usando map:", duplicados)  # [2, 4, 6, 8]
