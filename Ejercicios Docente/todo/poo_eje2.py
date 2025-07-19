# Ejercicio 2: Creación de instancias y métodos de comportamiento

class Libro:
    """
    Clase que representa un libro con sus atributos principales.
    """

    def __init__(self, titulo, autor, isbn, paginas):
        """
        Constructor de la clase Libro.
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

    def prestar_libro(self):
        """
        Método para prestar el libro. Cambia disponible a False si está disponible.
        """
        if self.disponible == True:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver_libro(self):
        """
        Método para devolver el libro. Cambia disponible a True si estaba prestado.
        """
        if self.disponible == False:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")


# 1. Definición de clase Libro (arriba) ✓

# 2. Crear dos objetos Libro diferentes
libro1 = Libro("El Principito", "Antoine de Saint-Exupéry", "978-3-14-046401-7", 120)
libro2 = Libro("Raza de Bronce", "Alcides Arguedas", "978-99905-2-213-9", 250)

# 3. Acceder y mostrar algunos de sus atributos directamente
print(f"\nEl autor del primer libro es: {libro1.autor}")
print(f"El ISBN del segundo libro es: {libro2.isbn}")

# 4. Llamar al método mostrar_info() para cada uno de los objetos
print("\n--- Mostrando información completa ---")
libro1.mostrar_info()
libro2.mostrar_info()

# 5. Añadir métodos de comportamiento (ya implementados arriba) ✓

# 6. Prueba los nuevos métodos con tus objetos libro1 y libro2
print("\n--- Probando métodos de comportamiento ---")

# Prestar libro1
libro1.prestar_libro()

# Intentar prestar libro1 otra vez (ya prestado)
libro1.prestar_libro()

# Devolver libro1
libro1.devolver_libro()

# Intentar devolver libro1 otra vez (ya disponible)
libro1.devolver_libro()

print("\n--- Probando con libro2 ---")

# Prestar libro2
libro2.prestar_libro()

# Devolver libro2
libro2.devolver_libro()

print("\n--- Estado final de los libros ---")
libro1.mostrar_info()
libro2.mostrar_info()