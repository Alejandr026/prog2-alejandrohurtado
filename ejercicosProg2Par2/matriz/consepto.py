matriz = [
    [10, 20, 30], #fila 0
    [40, 50, 60], #fila 1
    [70, 80 ,90]  #fila 2
]
#El primer indice selecciona la fila y el segundo el elemto de esta fila
valor = matriz[2][2]
#En este caso se toma la fila 2 que es [70, 80, 90] y se busca el valor 
# 90 que esta en el incide 2 de la fila
print (valor)
#Obtener las dimenciones
numero_filas = len(matriz)
numero_columnas = len(matriz[0])
print("Numero de filas: ", numero_filas)
print("Numero de columnas: ", numero_columnas)

"""
¿por qué len(matriz[0])?

Porque:

    matriz[0] accede a la primera fila: [10, 20, 30, 40]

    len(matriz[0]) cuenta cuántos elementos tiene esa fila → 4 columnas

    Por eso solo sirve cuando es regular o simetrica
"""