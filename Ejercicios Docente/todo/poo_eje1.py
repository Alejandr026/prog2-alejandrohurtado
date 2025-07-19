class Libro:
  """
  Clase que representa un libro con sus atributos principales.
  """

  def __init__(self, titulo, autor, isbn, paginas):
      """
      Constructor de la clase Libro.

      Args:
          titulo (str): Título del libro
          autor (str): Autor del libro
          isbn (str): ISBN del libro
          paginas (int): Número de páginas del libro
      """
      # Crear los atributos de instancia correspondientes
      self.titulo = titulo
      self.autor = autor
      self.isbn = isbn
      self.paginas = paginas

      # Atributo extra que se inicializa siempre por defecto
      self.disponible = True

  def mostrar_info(self):
      """
      Método que imprime todos los atributos del libro de forma clara y formateada.
      """
      print("=" * 50)
      print("INFORMACIÓN DEL LIBRO")
      print("=" * 50)
      print(f"Título: {self.titulo}")
      print(f"Autor: {self.autor}")
      print(f"ISBN: {self.isbn}")
      print(f"Páginas: {self.paginas}")
      print(f"Disponible: {'Sí' if self.disponible else 'No'}")
      print("=" * 50)


# Ejemplo de uso (no te preocupes por crear objetos todavía, ¡solo define la clase!)
if __name__ == "__main__":
  # Creación de ejemplo para demostrar el funcionamiento
  libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417)
  libro1.mostrar_info()

  # Cambiar disponibilidad
  libro1.disponible = False
  print("\nDespués de cambiar disponibilidad:")
  libro1.mostrar_info()