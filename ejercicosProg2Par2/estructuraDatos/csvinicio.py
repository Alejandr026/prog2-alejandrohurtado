import csv
datos = [{"nombre" : "Alejandro", "edad": 21, },
         {"nombre" : "Roberto", "edad": 20,}]
encabezados = ["nombre", "edad"]

with open("datos.csv", "w", newline="", encoding="utf-8") as archivo_csv:
    escritor = csv.DictWriter(archivo_csv, fieldnames=encabezados)
    escritor.writeheader()
    escritor.writerows(datos)


lista_leida = []
with open("datos.csv", "r", newline="", encoding="utf-8") as archivo_csv:
    lector = csv.DictReader(archivo_csv)
    for fila_dict in lector:
        fila_dict["edad"] = int(fila_dict["edad"])  # Convertir edad a int
        lista_leida.append(fila_dict)

# Mostrar lo leído
print(lista_leida)