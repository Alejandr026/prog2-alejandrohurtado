import tkinter as tk
from tkinter import messagebox

FILAS = 5
COLUMNAS = 6
asientos_ocupados = [(0, 1), (2, 3), (4, 0)]  # Ejemplo de asientos ocupados

class SalaCine:
    def _init_(self, master):
        self.master = master
        master.title("Sala de Cine")
        self.asientos = {}

        tk.Label(master, text="Selecciona tus asientos", font=("Arial", 14)).pack(pady=10)

        self.marco = tk.Frame(master)
        self.marco.pack()

        for fila in range(FILAS):
            for col in range(COLUMNAS):
                estado = (fila, col) in asientos_ocupados
                boton = tk.Button(self.marco, width=4, height=2,
                                  bg="red" if estado else "green",
                                  state="disabled" if estado else "normal")
                boton.grid(row=fila, column=col, padx=5, pady=5)
                boton.config(command=lambda f=fila, c=col, b=boton: self.seleccionar_asiento(f, c, b))
                self.asientos[(fila, col)] = boton

        self.seleccionados = []
        self.boton_confirmar = tk.Button(master, text="Confirmar Selección", command=self.confirmar)
        self.boton_confirmar.pack(pady=10)

    def seleccionar_asiento(self, fila, col, boton):
        if (fila, col) in self.seleccionados:
            self.seleccionados.remove((fila, col))
            boton.config(bg="green")
        else:
            self.seleccionados.append((fila, col))
            boton.config(bg="yellow")

    def confirmar(self):
        if not self.seleccionados:
            messagebox.showinfo("Información", "No seleccionaste ningún asiento.")
            return
        asientos = ", ".join([f"{chr(f + 65)}{c + 1}" for f, c in self.seleccionados])
        messagebox.showinfo("Reserva confirmada", f"Asientos seleccionados: {asientos}")
        for fila, col in self.seleccionados:
            self.asientos[(fila, col)].config(bg="red", state="disabled")
        self.seleccionados.clear()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Cine Interfaz")
ventana.geometry("400x400")
app = SalaCine(ventana)
ventana.mainloop()