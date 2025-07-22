import random

FILAS = 4
COLUMNAS = 2
BARCOS = 3

# Crear un tablero vacío
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Mostrar el tablero
def mostrar_tablero(tablero, ocultar_barcos=False):
    print("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
    for i, fila in enumerate(tablero):
        letra = chr(ord('A') + i)
        fila_mostrar = []
        for celda in fila:
            if ocultar_barcos and celda == 1:
                fila_mostrar.append("0")
            elif celda == 0:
                fila_mostrar.append("0")
            elif celda == 1:
                fila_mostrar.append("1")
            elif celda == 2:
                fila_mostrar.append("X")
            elif celda == 3:
                fila_mostrar.append("*")
        print(letra + " " + " ".join(fila_mostrar))

# Convertir coordenada tipo "A3" a índices [fila][columna]
def coord_a_indices(coord):
    fila = ord(coord[0].upper()) - ord('A')
    columna = int(coord[1:]) - 1
    return fila, columna

# Colocar barcos aleatoriamente
def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1

# Ejecutar disparo
def disparar(tablero_objetivo, tablero_disparos, coord, nombre):
    fila, columna = coord_a_indices(coord)
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        print(f"{nombre} hizo ¡Tocado!")
    elif tablero_objetivo[fila][columna] in [0]:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        print(f"{nombre} disparó al agua.")
    else:
        print("Ya se disparó allí.")

# Comprobar si quedan barcos
def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False

# Guardar puntuación
def guardar_puntuacion(nombre):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre} ganó la partida.\n")

# Menú principal del juego
def juego():
    print("=== Batalla Naval ===")
    print("1. Jugar contra la CPU")
    print("2. Jugar contra otro jugador")
    modo = input("Selecciona modo (1 o 2): ")

    if modo == "1":
        nombre_jugador = input("Tu nombre: ")
        nombre_cpu = "CPU"

        tablero_jugador = crear_tablero()
        tablero_cpu = crear_tablero()
        disparos_jugador = crear_tablero()
        disparos_cpu = crear_tablero()

        colocar_barcos(tablero_jugador, BARCOS)
        colocar_barcos(tablero_cpu, BARCOS)

        turno = 1
        while quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu):
            print(f"\n--- Turno {turno} ---")
            print("Tu tablero:")
            mostrar_tablero(tablero_jugador)
            print("Tus disparos:")
            mostrar_tablero(disparos_jugador)

            coord = input("Dispara (ej. A3): ")
            disparar(tablero_cpu, disparos_jugador, coord, nombre_jugador)

            # Turno CPU
            while True:
                fila_cpu = random.randint(0, FILAS - 1)
                col_cpu = random.randint(0, COLUMNAS - 1)
                if tablero_jugador[fila_cpu][col_cpu] in [0, 1]:
                    break
            coord_cpu = f"{chr(ord('A') + fila_cpu)}{col_cpu + 1}"
            print(f"{nombre_cpu} dispara a {coord_cpu}")
            disparar(tablero_jugador, disparos_cpu, coord_cpu, nombre_cpu)
            turno += 1

        if quedan_barcos(tablero_jugador):
            print(f"¡{nombre_jugador} gana!")
            guardar_puntuacion(nombre_jugador)
        else:
            print("¡La CPU gana!")

    elif modo == "2":
        nombre1 = input("Nombre del Jugador 1: ")
        nombre2 = input("Nombre del Jugador 2: ")

        tablero1 = crear_tablero()
        tablero2 = crear_tablero()
        disparos1 = crear_tablero()
        disparos2 = crear_tablero()

        colocar_barcos(tablero1, BARCOS)
        colocar_barcos(tablero2, BARCOS)

        turno = 1
        while quedan_barcos(tablero1) and quedan_barcos(tablero2):
            print(f"\n--- Turno {turno} ---")

            print(f"{nombre1}, este es tu turno")
            mostrar_tablero(disparos1)
            coord = input("Dispara (ej. A3): ")
            disparar(tablero2, disparos1, coord, nombre1)

            if not quedan_barcos(tablero2):
                break

            print(f"\n{nombre2}, este es tu turno")
            mostrar_tablero(disparos2)
            coord = input("Dispara (ej. A3): ")
            disparar(tablero1, disparos2, coord, nombre2)

            turno += 1

        if quedan_barcos(tablero2):
            print(f"¡{nombre1} gana!")
            guardar_puntuacion(nombre1)
        else:
            print(f"¡{nombre2} gana!")
            guardar_puntuacion(nombre2)
    else:
        print("Opción inválida. Reinicia el programa.")

# Ejecutar juego
juego()
