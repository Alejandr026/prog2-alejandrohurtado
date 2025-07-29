import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

ARCHIVO_SALA = "sala_guardada.json"

class SalaCine:
    def __init__(self, filas=5, columnas=8):
        self.filas = filas
        self.columnas = columnas
        self.sala = self.crear_sala()

    def crear_sala(self):
        sala = []
        for i in range(self.filas):
            fila = []
            for j in range(self.columnas):
                precio = 50 if 2 <= j <= 5 else 30
                fila.append({"estado": "L", "precio": precio})
            sala.append(fila)
        return sala

    def ocupar_asiento(self, fila, columna):
        asiento = self.sala[fila][columna]
        if asiento["estado"] == "L":
            asiento["estado"] = "O"
            return f"Asiento ({fila}, {columna}) reservado por Bs. {asiento['precio']}", True
        else:
            return "❌ Ese asiento ya está ocupado.", False

    def reservar_lista(self, lista_asientos):
        total = 0
        for fila, columna in lista_asientos:
            asiento = self.sala[fila][columna]
            asiento["estado"] = "O"
            total += asiento["precio"]
        return total

    def contar_libres(self):
        return sum(a["estado"] == "L" for fila in self.sala for a in fila)

    def guardar_estado(self):
        with open(ARCHIVO_SALA, "w") as f:
            json.dump(self.sala, f)
        return "💾 Sala guardada exitosamente."

    def cargar_estado(self):
        if os.path.exists(ARCHIVO_SALA):
            with open(ARCHIVO_SALA, "r") as f:
                self.sala = json.load(f)
            return "📂 Sala cargada correctamente."
        else:
            return "❌ No hay archivo guardado."

class InterfazCine:
    def __init__(self, root):
        self.root = root
        self.root.title("🎬 Sistema de Reserva de Cine")
        self.sala_cine = SalaCine()
        self.asientos_seleccionados = []

        self.frame_asientos = tk.Frame(root)
        self.frame_asientos.pack(pady=10)

        self.info_label = tk.Label(root, text="")
        self.info_label.pack()

        botones_frame = tk.Frame(root)
        botones_frame.pack(pady=10)

        tk.Button(botones_frame, text="Guardar Estado", command=self.guardar_sala).grid(row=0, column=0, padx=5)
        tk.Button(botones_frame, text="Cargar Estado", command=self.cargar_sala).grid(row=0, column=1, padx=5)
        tk.Button(botones_frame, text="Asientos Libres", command=self.mostrar_libres).grid(row=0, column=2, padx=5)
        tk.Button(botones_frame, text="Confirmar Reserva", command=self.confirmar_reserva).grid(row=0, column=3, padx=5)

        self.actualizar_interfaz()

    def actualizar_interfaz(self):
        for widget in self.frame_asientos.winfo_children():
            widget.destroy()

        for i in range(self.sala_cine.filas):
            for j in range(self.sala_cine.columnas):
                estado = self.sala_cine.sala[i][j]["estado"]
                if (i, j) in self.asientos_seleccionados:
                    color = "blue"
                elif estado == "L":
                    color = "green"
                else:
                    color = "red"

                btn = tk.Button(self.frame_asientos, text=f"{i},{j}", width=6, bg=color,
                                command=lambda i=i, j=j: self.toggle_asiento(i, j))
                btn.grid(row=i, column=j, padx=2, pady=2)

        self.info_label.config(text=f"Asientos libres: {self.sala_cine.contar_libres()}")

    def toggle_asiento(self, fila, columna):
        estado = self.sala_cine.sala[fila][columna]["estado"]
        if estado != "L":
            messagebox.showwarning("Ocupado", "Ese asiento ya está ocupado.")
            return

        if (fila, columna) in self.asientos_seleccionados:
            self.asientos_seleccionados.remove((fila, columna))
        else:
            self.asientos_seleccionados.append((fila, columna))
        self.actualizar_interfaz()

    def confirmar_reserva(self):
        if not self.asientos_seleccionados:
            messagebox.showinfo("Sin selección", "No has seleccionado ningún asiento.")
            return

        total = sum(self.sala_cine.sala[f][c]["precio"] for f, c in self.asientos_seleccionados)
        confirmar = messagebox.askyesno("Confirmar reserva", f"¿Deseas reservar {len(self.asientos_seleccionados)} asientos por Bs. {total}?")

        if confirmar:
            self.sala_cine.reservar_lista(self.asientos_seleccionados)
            self.asientos_seleccionados.clear()
            self.actualizar_interfaz()
            messagebox.showinfo("Reserva exitosa", f"🎟️ Has reservado tus asientos por Bs. {total}.")
        else:
            self.asientos_seleccionados.clear()
            self.actualizar_interfaz()

    def guardar_sala(self):
        mensaje = self.sala_cine.guardar_estado()
        messagebox.showinfo("Guardar", mensaje)

    def cargar_sala(self):
        mensaje = self.sala_cine.cargar_estado()
        self.asientos_seleccionados.clear()
        messagebox.showinfo("Cargar", mensaje)
        self.actualizar_interfaz()

    def mostrar_libres(self):
        libres = self.sala_cine.contar_libres()
        messagebox.showinfo("Asientos disponibles", f"Total de asientos libres: {libres}")

# Ejecutar programa
if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazCine(root)
    root.mainloop()

