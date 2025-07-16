#Libreria de funciones para vectores 
"""Funcion simple apara añadir elemetos a una lista en bucle"""
"""
COMO LLAMAR A LA FUNCION EJEMPLO:
from funVectores import añadirLista

Mylista = [1, 2, 3]
añadirLista(Mylista)
print(Mylista)
"""
def añadirLista(lista):
    while True:
        elegir = input("¿Deseas añadir más números a la lista? (s/n): ").strip().lower()
        if elegir == "s":
            try:
                numero = int(input("Ingrese un número para la lista: "))
                lista.append(numero)
            except ValueError:
                print("⚠️ Debes ingresar un número válido.")
        elif elegir == "n":
            break
        else:
            print("❌ Opción no válida. Escribe 's' o 'n'.")

    return lista

