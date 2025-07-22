#Ejercicio 2: leer nuestro diario
nombre_archivo = "diario.txt"

with open ("diario.txt", "a") as diario_file:
    diario_file.write("\n----Entrada del 22 de julio de 2025----\n")
    diario_file.write("El modo a es util para no perder los datos \n")
    diario_file.write("ahora se puede actualizar el diario\n")
print("Se guardaron las nuevas entradas")
