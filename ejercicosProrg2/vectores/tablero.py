# Crear tablero vacío
def crear_tablero():
    return [[" " for _ in range(3)] for _ in range(3)]

# Mostrar tablero en consola
def mostrar_tablero(tablero):
    print("\n  0   1   2")
    for i, fila in enumerate(tablero):
        print(i, " | ".join(fila))
        if i < 2:
            print("  ---+---+---")

# Verificar si hay ganador
def verificar_ganador(tablero, jugador):
    # Filas y columnas
    for i in range(3):
        if all(celda == jugador for celda in tablero[i]):
            return True
        if all(fila[i] == jugador for fila in tablero):
            return True

    # Diagonales
    if all(tablero[i][i] == jugador for i in range(3)):
        return True
    if all(tablero[i][2 - i] == jugador for i in range(3)):
        return True

    return False

# Verificar empate
def es_empate(tablero):
    return all(celda != " " for fila in tablero for celda in fila)

# Juego principal
def jugar():
    tablero = crear_tablero()
    jugador_actual = "X"

    while True:
        mostrar_tablero(tablero)
        print(f"\nTurno del jugador {jugador_actual}")
        try:
            fila = int(input("Ingresa la fila (0-2): "))
            columna = int(input("Ingresa la columna (0-2): "))
        except ValueError:
            print("❌ Ingresa solo números válidos.")
            continue

        if fila not in range(3) or columna not in range(3):
            print("❌ Posición fuera del tablero. Intenta de nuevo.")
            continue

        if tablero[fila][columna] != " ":
            print("❌ Esa casilla ya está ocupada. Intenta otra.")
            continue

        tablero[fila][columna] = jugador_actual

        if verificar_ganador(tablero, jugador_actual):
            mostrar_tablero(tablero)
            print(f"\n🎉 ¡Jugador {jugador_actual} ha ganado!")
            break
        elif es_empate(tablero):
            mostrar_tablero(tablero)
            print("\n🤝 ¡Empate!")
            break

        # Cambiar de jugador
        jugador_actual = "O" if jugador_actual == "X" else "X"

# Ejecutar el juego
jugar()


