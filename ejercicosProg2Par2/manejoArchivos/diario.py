#Ejercicio 1: creando y Escribiendo nuestro diario
nombre_archivo = "diario.txt"

with open ("diario.txt", "w") as diario:
    diario.write("Querido diario (reputo)\n")
    diario.write("hoy esoy aprendiendo a usar archivos en pyhton\n")
    diario.write("el modo w borra todo\n")
    diario.write("Pd: no te olivdes de quitar el reputo antes de presentar\n")

print()