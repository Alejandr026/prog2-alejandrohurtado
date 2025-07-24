class libro:
    def __init__(self, titulo_r, autor_r, isbn_r, paginas_r):
        self.titulo = titulo_r
        self.autor = autor_r
        self.isbn = isbn_r
        self.paginas = paginas_r
        self.disponible = True

    def mostrar_info(self):
        print(f"Informacion del libro {self.titulo}\n")
        print(f"Titulo: {self.titulo}\n Autor: {self.autor}\n Isbn: {self.isbn}\n Paginas: {self.paginas}\n Estado: {self.disponible}")
    
    def prestrar_libro(self):
        if self.disponible is True:
            self.disponible = False
            print(f"Acabas de prestar el libro {self.titulo}")
        elif self.disponible is  False:
            print(f"El libro {self.titulo} no esta disponible para prestamo")
    
    def devolver_libro(self):
        if self.disponible is False:
            self.disponible = True
            print(f"Acabas de devolver el libro {self.titulo}")
        elif self.disponible is  True:
            print(f"El libro {self.titulo} ya estaba disponible")


mi_biblioteca = []

libro1 = libro("Berserk Tomo 1", "Kentaro Miura", "978-4-7859-1972-4", 224)
libro2 = libro("Cien años de soledad", "Gabriel García Márquez", "978-84-376-0494-7", 432)
libro3 = libro("El Principito", "Antoine de Saint-Exupéry", "978-3-14-046401-7", 120)

mi_biblioteca.append(libro1)
mi_biblioteca.append(libro2)
mi_biblioteca.append(libro3)

for libro_actual in mi_biblioteca:
    libro_actual.mostrar_info()
    print("=" * 20)





