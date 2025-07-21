producto = {
    "codigo": "P001",
    "nombre": "Chocolate para Taza 'El Ceibo'",
    "precio_unitario": 15.50,
    "stock": 50,
    "proveedor":  "El Ceibo Ltda."
}

print("\n_____Precio de los productos_____\n")
print(f"{producto ['nombre']} : {producto['precio_unitario']}")

print("\n_____Stock de los productos_____\n")
print(f"{producto['nombre']} : {producto['stock']}")

producto["stock"] = 45

print("\n------Lista Actualizada------\n")

print("\n_____Precio de los productos_____\n")
print(f"{producto ['nombre']} : {producto['precio_unitario']}")

print("\n_____Stock de los productos_____\n")
print(f"{producto['nombre']} : {producto['stock']}")

producto["En oferta"] = True

print(producto)