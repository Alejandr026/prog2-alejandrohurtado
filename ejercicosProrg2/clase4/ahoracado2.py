import getpass, random

print("\n--- Bienvenido al juego del ahorcado numérico ---")
#print("Puedes hacer preguntas como: len(lis_secret), lis_secret[0], lis_secret[2] > 10, etc.")
print("\nCrea una lista secreta de numeros y que alguien intente adivinarlos")
print("\nCuando quieras intentar adivinar la lista, escribe 'adivinar'")
print("\n------------------------------------------------------------")

lis_secret = []
list_pista = []
while True:
    try:
        log_lista = int(input("Ingrese el tamaño de la lista secreta (no mayor a 10): "))
        if log_lista <= 0 or log_lista > 10:
            print("❌ Tamaño no válido. Intenta de nuevo.")
        else:
            for i in range(log_lista):
                numero = int(getpass.getpass(f"Ingrese el número #{i + 1}: "))
                lis_secret.append(numero)
                list_pista.append(0)
            print("✅ Lista secreta creada correctamente.")
            break 
    except ValueError:
        print("⚠️  Solo se permiten números enteros.")

while True:
    instruccion = input("\nDesea continuar s/n: ")

    if instruccion.strip().lower() == "s":
        intento = input("Escribe tu intento de lista (separada por comas): ")
        try:
            intento_lista = [int(x.strip()) for x in intento.split(",")]
            if intento_lista == lis_secret:
                print("🎉 ¡Correcto! Descubriste la lista secreta.")
                break
            else:
                print("❌ Esa no es la lista correcta. Sigue preguntando.")
                aleatorio = random.randint(0, len(lis_secret) - 1)
                pista = lis_secret[aleatorio]
                print(f"🔎 Pista: El valor en la posición {aleatorio + 1} es {pista}")
                list_pista[aleatorio] = pista
                print(list_pista)
        except ValueError:
            print("⚠️ Error: asegúrate de escribir solo números separados por comas.")
    else:
        try:
            resultado = eval(instruccion, {"lis_secret": lis_secret})
            print("🔎 Resultado:", resultado)
        except Exception as e:
            print("❌ Error en tu instrucción:", e)

              