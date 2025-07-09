# Alejandro Hurtado
def clas_movie(var1):
  if var1 < 0:
    return "Edad no valida"
  elif var1 < 13:
    return "Te recomendamos peliculas clasificaion G o PG"
  elif var1 < 18:
    return "Podes ver peliculas clasificaion PG-13"
  else:
    return "Puedes ver cualquier pelicula (Clisificaion R)"


# Pruebas Unitarias para el programa edad.py
assert clas_movie(12) == "Te recomendamos peliculas clasificaion G o PG", "Error de edad 12"
assert clas_movie(15) == "Podes ver peliculas clasificaion PG-13", "Error de edad 15"  
assert clas_movie(20) == "Puedes ver cualquier pelicula (Clisificaion R)", "Error de edad 20"
assert clas_movie(-5) == "Edad no valida", "Error de edad Negativa"

# Fin de la funcion clas_movie
while True:
  try:
    edad = int(input("Ingrese su edad: "))
    resultado = clas_movie(edad)
    print(resultado)
  except ValueError:
    print("Error: Ingrese un numero entero valido")
    continue

  continuar = input("¿verificar otra edad? (s/n): ").strip().lower()
  if continuar != "s":
    break

print("Fin del programa")
print("_____Alejandro Hurtado_____")

