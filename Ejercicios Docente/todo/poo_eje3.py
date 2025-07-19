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
      self.titulo = titulo
      self.autor = autor
      self.isbn = isbn
      self.paginas = paginas
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


if __name__ == "__main__":
  # Crear objetos de tipo Libro
  libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", 417)
  libro2 = Libro("1984", "George Orwell", "978-0451524935", 328)
  libro3 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-0156013987", 96)

  # Crear una lista vacía
  mi_biblioteca = []

  # Añadir libros a la lista
  mi_biblioteca.append(libro1)
  mi_biblioteca.append(libro2)
  mi_biblioteca.append(libro3)

  # Mostrar el inventario completo
  print("\n\n--- INVENTARIO COMPLETO DE LA BIBLIOTECA ---")
  for libro_actual in mi_biblioteca:
      libro_actual.mostrar_info()
      print("=" * 20)  # Separador