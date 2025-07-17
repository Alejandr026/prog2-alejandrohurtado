# 1. Crear el diccionario 'producto'
producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor": "El Ceibo Ltda."
}

# 2. Imprimir nombre y precio del producto
print(f"Producto: {producto['nombre']}")
print(f"Precio unitario: Bs. {producto['precio_unitario']}")

# 3. Simular una venta: restar 5 unidades del stock
producto["stock"] -= 5

# 4. Añadir clave "en_oferta" con valor True
producto["en_oferta"] = True

# 5. Imprimir el diccionario completo con todos los cambios
print("\nEstado final del producto:")
for clave, valor in producto.items():
    print(f"{clave}: {valor}")
