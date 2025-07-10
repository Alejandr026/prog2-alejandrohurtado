#Lista donde se guardan las comidas 
comida_fav = ["Salteña", "Cuñape", "Sopa de Mani"]
print(comida_fav)

print("\nMi segunda comida favorita es " + comida_fav[1])
print("\nCambiar tu primera comida favorita")
nueva_comida = input("\nIngresa tu nueva comida favorita:")
comida_fav[0] = nueva_comida
print(comida_fav)
cantidad_comida = len(comida_fav)
print(f"\nLa cantidad de comidas favoritas que tienes es de {cantidad_comida}")