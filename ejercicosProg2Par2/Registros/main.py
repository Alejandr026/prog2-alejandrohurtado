producto = {
    "codigo" : "P001",
    "nombre" : "Cafe el Patron",
    "precio" : 30.50,
}
print(f"Nombre del producto {producto ['nombre']}")
producto["precio"] = 38.50
print(f"El nuevo precio del cafe es de {producto['precio']}")
producto["stock"] = 100

print(f"diccionario actualizado {producto}")
del producto["precio"]
print(f"\ndiccionario actualizado sin precio {producto}")

producto = {'codigo': 'P001', 'nombre': 'Café', 'precio': 38.0, 'stock': 100}
print("\n--- Claves del producto ---")
for clave in producto: # Por defecto, itera sobre las CLAVES
    print(clave)
print("\n--- Clave y Valor ---")
for clave in producto:
        valor = producto[clave]
        print(f"{clave.capitalize()}: {valor}")