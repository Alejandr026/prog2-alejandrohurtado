import csv

# Datos a escribir
datos = [{"nombre": "Ana", "edad": 20},
         {"nombre": "Luis", "edad": 22}]

encabezados = ["nombre", "edad"]

# Escribir en el archivo CSV
with open("datos.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor.writeheader()         # Escribe los encabezados
    escritor.writerows(datos)      # Escribe todos los diccionarios

# Leer el archivo CSV
lista_leida = []
with open("datos.csv", "r", newline="", encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila_dict in lector:
        fila_dict["edad"] = int(fila_dict["edad"])  # Convertir edad a int
        lista_leida.append(fila_dict)

# Mostrar lo leído
print(lista_leida)
