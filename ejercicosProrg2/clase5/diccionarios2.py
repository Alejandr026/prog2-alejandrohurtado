# 1. Crear una lista vacía llamada inventario
inventario = []

# 2. Crear al menos tres diccionarios de productos diferentes
producto1 = {
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "stock": 50
}

producto2 = {
    "nombre": "Café de los Yungas",
    "stock": 100
}

producto3 = {
    "nombre": "Quinua Real en Grano",
    "stock": 80
}

# 3. Añadir los productos al inventario
inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

# 4. Imprimir cantidad de tipos de producto
print(f"\nCantidad de productos en inventario: {len(inventario)}")

# 5. Recorrer el inventario e imprimir resumen
print("\n--- Inventario Actual ---")
for producto in inventario:
    print(f"- {producto['nombre']}: {producto['stock']} unidades en stock.")
