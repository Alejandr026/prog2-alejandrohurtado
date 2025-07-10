def clas_pelicula(edad):
    if edad < 0:
        return "Edad no válida."
    elif edad >= 18:
        return "¡Puedes ver películas clasificadas R!"
    elif edad >= 13:
        return "Puedes ver películas clasificadas PG-13."
    else:
        return "Te recomendamos películas clasificadas G o PG."

# Casos de prueba
print("Ejecutando pruebas...")
assert clas_pelicula(20) == "¡Puedes ver películas clasificadas R!", "Prueba fallida: Adulto"
assert clas_pelicula(18) == "¡Puedes ver películas clasificadas R!", "Prueba fallida: Límite Adulto"
assert clas_pelicula(15) == "Puedes ver películas clasificadas PG-13.", "Prueba fallida: Adolescente"
assert clas_pelicula(13) == "Puedes ver películas clasificadas PG-13.", "Prueba fallida: Límite Adolescente"
assert clas_pelicula(10) == "Te recomendamos películas clasificadas G o PG.", "Prueba fallida: Niño"
assert clas_pelicula(-5) == "Edad no válida.", "Prueba fallida: Edad negativa"
print("¡Todas las pruebas pasaron exitosamente! Nuestra función es robusta. 🎉")

# Parte interactiva
while True:
    try:
        edad = int(input("Ingrese su edad: "))
        resultado = clas_pelicula(edad)
        print(resultado)
    except ValueError:
        print("Error: Ingrese un número entero válido.")
        continue

    continuar = input("¿Verificar otra edad? (s/n): ").strip().lower()
    if continuar != "s":
        break

print("Fin del programa")
print("_____Alejandro Hurtado_____")


