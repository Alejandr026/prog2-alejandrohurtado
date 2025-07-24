class Estudiante:
    def __init__(self, nombre_ingresado, edad_ingresada, carrera_ingresada):
        print(f"Creando un nuevo estudiante llamado {nombre_ingresado}")
        self.nombre = nombre_ingresado
        self.edad = edad_ingresada
        self.carrera = carrera_ingresada
        self.materias = []
        
    
    def presemtarse(self):
        print(f"Hola soy {self.nombre} tengo {self.edad} años y estudio la carrera de {self.carrera}")
    
    def inscribir_materia(self, nombre_materia):
        self.materias.append(nombre_materia)
        print(f"{self.nombre} se inscribio a {nombre_materia}")    

Estudiante1 = Estudiante("Alejandro", 21, "Ing.Telecomunicaiones")
Estudiante1.inscribir_materia("Redes 2")

Estudiante1.presemtarse()

print(Estudiante1.nombre)
print(Estudiante1.carrera)