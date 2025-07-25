class Producto:
  """
  Clase que representa un producto en la tienda online.
  """

  def __init__(self, nombre, precio, disponible=True):
      """
      Constructor de la clase Producto.

      Args:
          nombre (str): Nombre del producto
          precio (float): Precio del producto
          disponible (bool): Disponibilidad del producto (por defecto True)
      """
      self.nombre = nombre
      self.precio = precio
      self.disponible = disponible

  def mostrar_info(self):
      """
      Método que imprime la información del producto.
      """
      print("=" * 50)
      print(f"Producto: {self.nombre}")
      print(f"Precio: ${self.precio:.2f}")
      print(f"Disponible: {'Sí' if self.disponible else 'No'}")
      print("=" * 50)


class Cliente:
  """
  Clase que representa a un cliente de la tienda online.
  """

  def __init__(self, nombre, direccion):
      """
      Constructor de la clase Cliente.

      Args:
          nombre (str): Nombre del cliente
          direccion (str): Dirección del cliente
      """
      self.nombre = nombre
      self.direccion = direccion
      self.carrito = CarritoDeCompras()  # Cada cliente tiene un carrito

  def ver_carrito(self):
      """
      Muestra los productos en el carrito de compras del cliente.
      """
      print(f"\nCarrito de {self.nombre}:")
      self.carrito.mostrar_carrito()

  def realizar_compra(self):
      """
      Método que simula la realización de una compra.
      """
      total = self.carrito.calcular_total()
      print(f"\nTotal de la compra: ${total:.2f}")
      self.carrito.vaciar_carrito()  # Vaciar el carrito después de la compra
      print(f"\nCompra realizada por {self.nombre}.")


class CarritoDeCompras:
  """
  Clase que representa el carrito de compras de un cliente.
  """

  def __init__(self):
      """
      Constructor de la clase CarritoDeCompras. Inicializa un carrito vacío.
      """
      self.productos = []

  def agregar_producto(self, producto):
      """
      Método para agregar un producto al carrito.

      Args:
          producto (Producto): El producto que se agregará al carrito
      """
      if producto.disponible:
          self.productos.append(producto)
          print(f"\n{producto.nombre} ha sido agregado al carrito.")
      else:
          print(f"\nLo siento, {producto.nombre} no está disponible.")

  def mostrar_carrito(self):
      """
      Muestra los productos en el carrito.
      """
      if not self.productos:
          print("El carrito está vacío.")
      else:
          for producto in self.productos:
              producto.mostrar_info()

  def calcular_total(self):
      """
      Calcula el total de la compra.
      """
      total = sum([producto.precio for producto in self.productos])
      return total

  def vaciar_carrito(self):
      """
      Vacía el carrito de compras.
      """
      self.productos = []
      print("\nEl carrito ha sido vaciado.")


# Ejemplo de uso del sistema
if __name__ == "__main__":
  # Crear algunos productos de ejemplo
  producto1 = Producto("Camiseta Roja", 19.99)
  producto2 = Producto("Pantalón Azul", 39.99)
  producto3 = Producto("Zapatillas Deportivas", 59.99, disponible=False)  # Producto no disponible

  # Crear un cliente
  cliente1 = Cliente("Juan Pérez", "Calle Ficticia 123")

  # Cliente agrega productos a su carrito
  cliente1.carrito.agregar_producto(producto1)
  cliente1.carrito.agregar_producto(producto2)
  cliente1.carrito.agregar_producto(producto3)  # Producto no disponible

  # Ver el carrito
  cliente1.ver_carrito()

  # Realizar la compra
  cliente1.realizar_compra()

  # Ver el carrito después de la compra
  cliente1.ver_carrito()
