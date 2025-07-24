import csv

inventario = [
    {"nombre": "cafe", "precio": 25.70, "stock": 50},
    {"nombre": "coca cola", "precio": 12.00, "stock": 100},
    {"nombre": "monster", "precio": 15.50, "stock": 80}
]

encabezados = ["nombre", "precio", "stock"]

with open("inventario.csv", "w", newline="", encoding="utf-8") as archivo_inventario:
    escribir = csv.DictWriter(archivo_inventario, fieldnames=encabezados)
    escribir.writeheader()
    escribir.writerows(inventario)
    print("✅ Se añadieron los datos al archivo inventario.csv")

inventario_cargado_csv = []

with open("inventario.csv", "r", newline="", encoding="utf-8") as archivo_inventario:
    leer = csv.DictReader(archivo_inventario)
    for item in leer:
        item["precio"] = float(item["precio"])
        item["stock"] = int(item["stock"])
        inventario_cargado_csv.append(item)

print("\n📦 Inventario cargado desde CSV:")
for producto in inventario_cargado_csv:
    print(producto)



