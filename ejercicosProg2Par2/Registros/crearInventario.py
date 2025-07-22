inventario = []

producto1 = {
    "nombre" : "cafe",
    "precio" : 25.70,
    "Stock" : 50
}

producto2 = {
    "nombre" : "coca cola",
    "precio" : 12.00,
    "Stock" : 100
}

producto3 = {
    "nombre" : "monster",
    "precio" : 15.50,
    "Stock" : 80
}

inventario.append(producto1)
inventario.append(producto2)
inventario.append(producto3)

cantidad = len(inventario)
""" 
for i in range(cantidad):
    print("\nInventario actual")
    print(f"Producto {i+1}:")
    print(f"Nombre: {inventario[i]['nombre'].capitalize()}")
    print(f"Precio: Bs {inventario[i]['precio']}")
    print(f"Stock: {inventario[i]['Stock']} unidades")
"""
for i in range(len(inventario)):
    for clave, valor in inventario[i].items():
        print(f"{clave} : {valor}")
        
for k in producto1.keys():
    print (k)
