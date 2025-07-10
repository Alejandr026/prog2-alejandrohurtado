from funciones import clas_movie

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