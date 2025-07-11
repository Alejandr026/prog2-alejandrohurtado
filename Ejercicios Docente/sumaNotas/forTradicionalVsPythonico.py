#CALCULO DEL CUADRADO DE LOS ELEMENTOS DE UNA LISTA DEL 0 AL 4
cuadrados = []
# TRADICIONAL
for x in range(5):
    cuadrados.append(x * x)
print(cuadrados)  # [0, 1, 4, 9, 16]
#PYTHONICO
cuadrados = [x * x for x in range(5)]
print(cuadrados)  # [0, 1, 4, 9, 16]
