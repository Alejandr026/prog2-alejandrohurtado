import tkinter as tk
from tkinter import scrolledtext
import random

FILAS = 4
COLUMNAS = 4
BARCOS = 3

# Variables globales
entrada_usuario = None
entrada_valor = ""
esperando_input = False

# Crear tablero vacío
def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

# Mostrar tablero en consola embebida
def mostrar_tablero(tablero, ocultar_barcos=False):
    escribir("  " + " ".join(str(i + 1) for i in range(COLUMNAS)))
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
        escribir(letra + " " + " ".join(fila_mostrar))

def coord_a_indices(coord):
    fila = ord(coord[0].upper()) - ord('A')
    columna = int(coord[1:]) - 1
    return fila, columna

def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1

def disparar(tablero_objetivo, tablero_disparos, coord, nombre):
    fila, columna = coord_a_indices(coord)
    if tablero_objetivo[fila][columna] == 1:
        tablero_objetivo[fila][columna] = 2
        tablero_disparos[fila][columna] = 2
        escribir(f"{nombre} ¡Acerto a un Barco!")
    elif tablero_objetivo[fila][columna] == 0:
        tablero_objetivo[fila][columna] = 3
        tablero_disparos[fila][columna] = 3
        escribir(f"{nombre} disparó al agua.")
    else:
        escribir("Ya se disparó allí.")

def quedan_barcos(tablero):
    for fila in tablero:
        if 1 in fila:
            return True
    return False

def guardar_puntuacion(nombre):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre} ganó la partida.\n")

# Reemplazo de input()
def pedir_input(mensaje, callback):
    global esperando_input
    esperando_input = True
    escribir(mensaje)
    entrada_usuario.config(state="normal")
    entrada_usuario.delete(0, tk.END)
    entrada_usuario.focus()

    def leer():
        global esperando_input
        entrada = entrada_usuario.get().strip()
        entrada_usuario.delete(0, tk.END)
        entrada_usuario.config(state="disabled")
        esperando_input = False
        callback(entrada)

    boton_enviar.config(command=leer)

# Redefinir print
def escribir(texto):
    consola.config(state="normal")
    consola.insert(tk.END, texto + "\n")
    consola.see(tk.END)
    consola.config(state="disabled")

# Lógica simplificada del juego contra CPU
def iniciar_juego():
    def paso_nombre(nombre):
        jugador = nombre
        cpu = "CPU"
        tablero_jugador = crear_tablero()
        tablero_cpu = crear_tablero()
        disparos_jugador = crear_tablero()
        disparos_cpu = crear_tablero()
        colocar_barcos(tablero_jugador, BARCOS)
        colocar_barcos(tablero_cpu, BARCOS)

        turno = [1]

        def turno_jugador():
            if not (quedan_barcos(tablero_jugador) and quedan_barcos(tablero_cpu)):
                terminar_partida()
                return

            escribir(f"\n--- Turno {turno[0]} ---")
            escribir("Tu tablero:")
            mostrar_tablero(tablero_jugador)
            escribir("Tus disparos:")
            mostrar_tablero(disparos_jugador)

            pedir_input("Dispara (ej. A1):", lambda coord: ejecutar_disparo(coord, jugador))

        def ejecutar_disparo(coord, jugador):
            try:
                disparar(tablero_cpu, disparos_jugador, coord, jugador)
            except:
                escribir("⚠️ Coordenada inválida.")
                turno_jugador()
                return

            disparo_cpu()
            turno[0] += 1
            ventana.after(500, turno_jugador)

        def disparo_cpu():
            while True:
                fila = random.randint(0, FILAS - 1)
                col = random.randint(0, COLUMNAS - 1)
                if tablero_jugador[fila][col] in [0, 1]:
                    break
            coord = f"{chr(ord('A') + fila)}{col + 1}"
            escribir(f"CPU dispara a {coord}")
            disparar(tablero_jugador, disparos_cpu, coord, "CPU")

        def terminar_partida():
            if quedan_barcos(tablero_jugador):
                escribir("🎉 ¡Ganaste!")
                guardar_puntuacion(jugador)
            else:
                escribir("💀 La CPU gana.")
            escribir("Fin del juego.")

        turno_jugador()

    consola.config(state="normal")
    consola.delete(1.0, tk.END)
    consola.config(state="disabled")
    pedir_input("Ingresa tu nombre:", paso_nombre)

# INTERFAZ
ventana = tk.Tk()
ventana.title("Batalla Naval")
ventana.geometry("600x500")

tk.Label(ventana, text="Batalla Naval", font=("Arial", 16)).pack()

consola = scrolledtext.ScrolledText(ventana, height=20, state="disabled", bg="black", fg="lime", font=("Courier", 10))
consola.pack(padx=10, pady=10, fill="both", expand=True)

entrada_usuario = tk.Entry(ventana, font=("Arial", 12), state="disabled")
entrada_usuario.pack(pady=5)

boton_enviar = tk.Button(ventana, text="Enviar", state="normal")
boton_enviar.pack()

boton_iniciar = tk.Button(ventana, text="Iniciar Juego contra CPU", command=iniciar_juego)
boton_iniciar.pack(pady=10)

ventana.mainloop()
