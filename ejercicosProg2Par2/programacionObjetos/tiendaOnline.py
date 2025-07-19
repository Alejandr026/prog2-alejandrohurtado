class producto:
    def __init__(self, nombre, precio, disponible):
        self.nombre = nombre
        self.precio = precio
        self.disponible = True

    def mostrar_info(self):
        print("=" * 50)
        print("INFORMACIÓN DEL PRODUCTO")
        print("=" * 50)
        print(f"Nombre: {self.nombre}")
        print(f"Precio: {self.precio}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print("=" * 50)

class cliente:
  def __init__(self, nombre, direccion, carrito):
    self.nombre = nombre
    self.direccion = direccion  
    self.carrito = []

  def ver_carrito(self):
    print("=" * 50)
    print("CARRITO DE COMPRAS")
    print("=" * 50)
    for producto in self.carrito:
      producto.mostrar_info()

  def realizar_compra(self):
    print("=" * 50)
    print("COMPRA REALIZADA")
    print("=" * 50)
    total = 0
    for producto in self.carrito:
      total += producto.precio
    
    print(f"Total: {total}")