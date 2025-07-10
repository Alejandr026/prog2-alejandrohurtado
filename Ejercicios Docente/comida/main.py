from funciones import imprimir_lista, modificar_lista

comidas_favoritas = ['Pizza', 'Sushi', 'Tacos']

def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1. Ver lista de comidas favoritas")
        print("2. Modificar una comida")
        print("3. Salir")
        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            imprimir_lista(comidas_favoritas)
        elif opcion == '2':
            modificar_lista(comidas_favoritas)
        elif opcion == '3':
            print("👋 ¡Hasta luego!")
            break
        else:
            print("❌ Opción no válida. Intenta de nuevo.")

menu()
