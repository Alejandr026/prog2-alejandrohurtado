class Producto:
    def __init__(self, nombre, precio, disponible=True):
        self.nombre = nombre
        self.precio = precio
        self.disponible = disponible

    def mostrar_info(self):
        print("=" * 50)
        print(f"Producto: {self.nombre}")
        print(f"Precio: ${self.precio:.2f}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")
        print("=" * 50)


class Cliente:
    def __init__(self, nombre, direccion):
        self.nombre = nombre
        self.direccion = direccion
        self.carrito = CarritoDeCompras()

    def ver_carrito(self):
        print(f"\nCarrito de {self.nombre}:")
        self.carrito.mostrar_carrito()

    def realizar_compra(self):
        total = self.carrito.calcular_total()
        print(f"\nTotal de la compra: ${total:.2f}")
        self.carrito.vaciar_carrito()
        print(f"\nCompra realizada por {self.nombre}.")


class CarritoDeCompras:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if producto.disponible:
            self.productos.append(producto)
            print(f"\n{producto.nombre} ha sido agregado al carrito.")
        else:
            print(f"\nLo siento, {producto.nombre} no está disponible.")

    def mostrar_carrito(self):
        if not self.productos:
            print("El carrito está vacío.")
        else:
            for producto in self.productos:
                producto.mostrar_info()

    def calcular_total(self):
        total = sum([producto.precio for producto in self.productos])
        return total

    def vaciar_carrito(self):
        self.productos = []
        print("\nEl carrito ha sido vaciado.")


if __name__ == "__main__":
    producto1 = Producto("Camiseta Roja", 50.99)
    producto2 = Producto("Pantalón Negro", 140.99)
    producto3 = Producto("Zapatillas Nike Jordan", 299.99, disponible=False)

    cliente1 = Cliente("Alejandro", "Paragua cnlf Perez")

    cliente1.carrito.agregar_producto(producto1)
    cliente1.carrito.agregar_producto(producto2)
    cliente1.carrito.agregar_producto(producto3)

    cliente1.ver_carrito()
    cliente1.realizar_compra()
    cliente1.ver_carrito()

