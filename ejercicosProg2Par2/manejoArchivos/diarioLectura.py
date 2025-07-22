#Ejercicio 2: leer nuestro diario
nombre_archivo = "diario.txt"

#Opcion A: Leer todo de golpe
"""with open ("diario.txt", "r") as diario:
    contenido = diario.read()

print(contenido)"""
print("\n--- Contenido del diario (línea por línea) ---")
try:
    with open ("diario.txt", "r") as diario:
        for linea in diario:
            print(linea.strip()) #strip quita los \n extras
except FileExistsError:
    print(f"Error: El archivo '{nombre_archivo}' no existe")

with open ("diario.txt", "a") as diario_file:
    diario_file.write("\n----Entrada del 22 de julio de 2025----\n")
    diario_file.write("El modo a es util para no perder los datos \n")
    diario_file.write("ahora se puede actualizar el diario\n")
print("Se guardaron las nuevas entradas")