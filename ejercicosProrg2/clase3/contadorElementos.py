#Contador de cuntas veces aparece un elementon de una lista 

palabra = "hola mundo"
contador = 0

for i in palabra:
    if i == "o":
        contador = contador + 1
print(f"El numero de veces que se repite la o es de: {contador}")