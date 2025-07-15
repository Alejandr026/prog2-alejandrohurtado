#Prueba simple de añadir elementos a una lista

lista = [1, 2, 3]
while True:
    elegir = input("Desea añador mas numeros a la lista s/n: ")
    if elegir == "s":
        añadir = int(input("Ingrese un numero para la lista: "))
        lista.append(añadir)
    else:
        break
    

print(lista)