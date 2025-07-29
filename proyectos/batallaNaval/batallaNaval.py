import tkinter as tk
from tkinter import messagebox, simpledialog
import random
import os

FILAS = 4
COLUMNAS = 4
BARCOS = 3

def crear_tablero():
    return [[0 for _ in range(COLUMNAS)] for _ in range(FILAS)]

def colocar_barcos(tablero, cantidad):
    colocados = 0
    while colocados < cantidad:
        fila = random.randint(0, FILAS - 1)
        columna = random.randint(0, COLUMNAS - 1)
        if tablero[fila][columna] == 0:
            tablero[fila][columna] = 1
            colocados += 1

def quedan_barcos(tablero):
    return any(1 in fila for fila in tablero)

def guardar_puntuacion(nombre):
    with open("puntuaciones.txt", "a") as archivo:
        archivo.write(f"{nombre} ganó la partida.\n")

class BatallaNavalGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🚢 Batalla Naval")
        self.modo = None
        self.jugador1 = ""
        self.jugador2 = ""
        self.turno = 1
        self.turno_actual = 1  # 1 o 2

        self.crear_pantalla_inicio()

    def crear_pantalla_inicio(self):
        self.limpiar_pantalla()

        tk.Label(self.root, text="🚢 Batalla Naval", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.root, text="Selecciona un modo de juego").pack(pady=5)

        tk.Button(self.root, text="Jugador vs CPU", command=self.iniciar_vs_cpu).pack(pady=5)
        tk.Button(self.root, text="Jugador vs Jugador", command=self.iniciar_vs_jugador).pack(pady=5)

    def iniciar_vs_cpu(self):
        self.modo = "cpu"
        self.jugador1 = simpledialog.askstring("Nombre", "Ingresa tu nombre:")
        self.jugador2 = "CPU"
        self.inicializar_tableros()
        self.crear_interfaz_juego()

    def iniciar_vs_jugador(self):
        self.modo = "jugador"
        self.jugador1 = simpledialog.askstring("Jugador 1", "Nombre del Jugador 1:")
        self.jugador2 = simpledialog.askstring("Jugador 2", "Nombre del Jugador 2:")
        self.inicializar_tableros()
        self.crear_interfaz_juego()

    def inicializar_tableros(self):
        self.tablero1 = crear_tablero()
        self.tablero2 = crear_tablero()
        self.disparos1 = crear_tablero()
        self.disparos2 = crear_tablero()
        colocar_barcos(self.tablero1, BARCOS)
        colocar_barcos(self.tablero2, BARCOS)

    def crear_interfaz_juego(self):
        self.limpiar_pantalla()

        self.label_turno = tk.Label(self.root, text="", font=("Arial", 12))
        self.label_turno.pack(pady=5)

        self.frame_tablero = tk.Frame(self.root)
        self.frame_tablero.pack()

        self.botones = [[None for _ in range(COLUMNAS)] for _ in range(FILAS)]
        for i in range(FILAS):
            for j in range(COLUMNAS):
                btn = tk.Button(self.frame_tablero, text=f"{chr(ord('A')+i)}{j+1}", width=4, height=2,
                                command=lambda i=i, j=j: self.disparar(i, j))
                btn.grid(row=i, column=j, padx=2, pady=2)
                self.botones[i][j] = btn

        self.actualizar_tablero()

    def actualizar_tablero(self):
        self.label_turno.config(text=f"Turno {self.turno} - {self.jugador1 if self.turno_actual == 1 else self.jugador2}")

        actual = self.disparos1 if self.turno_actual == 1 else self.disparos2
        for i in range(FILAS):
            for j in range(COLUMNAS):
                estado = actual[i][j]
                if estado == 0:
                    color = "lightgray"
                elif estado == 2:
                    color = "red"
                elif estado == 3:
                    color = "blue"
                else:
                    color = "gray"
                self.botones[i][j].config(bg=color)

    def disparar(self, fila, columna):
        actual_disp = self.disparos1 if self.turno_actual == 1 else self.disparos2
        objetivo = self.tablero2 if self.turno_actual == 1 else self.tablero1
        nombre = self.jugador1 if self.turno_actual == 1 else self.jugador2

        if actual_disp[fila][columna] in [2, 3]:
            messagebox.showinfo("Ya disparaste", "Ya disparaste en esa celda.")
            return

        if objetivo[fila][columna] == 1:
            actual_disp[fila][columna] = 2
            objetivo[fila][columna] = 2
            messagebox.showinfo("Resultado", "🎯 ¡Tocado!")
        else:
            actual_disp[fila][columna] = 3
            objetivo[fila][columna] = 3
            messagebox.showinfo("Resultado", "💦 Agua")

        if not quedan_barcos(objetivo):
            ganador = nombre
            guardar_puntuacion(ganador)
            messagebox.showinfo("Fin del juego", f"🎉 ¡{ganador} gana!")
            self.root.quit()
            return

        self.turno += 1

        if self.modo == "cpu" and self.turno_actual == 1:
            self.turno_actual = 2
            self.actualizar_tablero()
            self.root.after(800, self.disparo_cpu)
        else:
            self.turno_actual = 1 if self.turno_actual == 2 else 2
            self.actualizar_tablero()

    def disparo_cpu(self):
        while True:
            f = random.randint(0, FILAS - 1)
            c = random.randint(0, COLUMNAS - 1)
            if self.tablero1[f][c] in [0, 1]:
                break

        if self.tablero1[f][c] == 1:
            self.tablero1[f][c] = 2
            self.disparos2[f][c] = 2
            print(f"CPU acertó en {chr(ord('A')+f)}{c+1}")
        else:
            self.tablero1[f][c] = 3
            self.disparos2[f][c] = 3
            print(f"CPU falló en {chr(ord('A')+f)}{c+1}")

        if not quedan_barcos(self.tablero1):
            guardar_puntuacion(self.jugador2)
            messagebox.showinfo("Fin del juego", f"🎉 ¡{self.jugador2} gana!")
            self.root.quit()
            return

        self.turno += 1
        self.turno_actual = 1
        self.actualizar_tablero()

    def limpiar_pantalla(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# === Ejecutar programa ===
if __name__ == "__main__":
    root = tk.Tk()
    app = BatallaNavalGUI(root)
    root.mainloop()
