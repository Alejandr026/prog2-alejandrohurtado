from datetime import datetime

nombre_archivo = "diario.txt"

while True:
    print("¿Quieres añadir una nueva entrada al diario?")
    print("1: Sí")
    print("2: No")
    print("3: Ver diario")
    entrada = input("Elige una opción: ")

    if entrada == "1":
        with open(nombre_archivo, "a") as diario_file:
            entrada_texto = input("\nEscriba su nueva entrada: ")
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            diario_file.write(f"\nFecha de la entrada: {fecha_hora}\n")
            diario_file.write(f"{entrada_texto} \n")
            
        print("✅ Se guardó la nueva entrada.")
        
    elif entrada == "2":
        print("Adios.")
        break

    elif entrada == "3":
        print("\n========== Contenido del diario ==========\n")
        try:
            with open(nombre_archivo, "r") as diario:
                for linea in diario:
                    print(linea.strip())
        except FileNotFoundError:
            print(f"⚠️ Error: El archivo '{nombre_archivo}' no existe.")
    else:
        print("❌ Opción no válida.")
