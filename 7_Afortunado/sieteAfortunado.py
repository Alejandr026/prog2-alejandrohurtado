from tkinter import *
import random
import sys
import os

def obtener_ruta_recurso(rel_path):
    """Obtiene la ruta absoluta al recurso, compatible con PyInstaller"""
    try:
        base_path = sys._MEIPASS  # Ruta temporal creada por PyInstaller
    except Exception:
        base_path = os.path.abspath(".")  # Ruta actual al ejecutar como script
    return os.path.join(base_path, rel_path)

class SieteAfortunado:

    def __init__(self):
        self.crear_interfaz()

    def crear_interfaz(self):
        self.ventana = Tk()
        self.ventana.minsize(340,450)
        self.ventana.geometry('340x450')

        boton = Button(self.ventana, text="Jugar!", command=self.jugar, font='arial 18 bold')
        boton.pack()

        ruta_imagen = obtener_ruta_recurso("dinero.png")
        self.foto = PhotoImage(file=ruta_imagen)
        self.gano = Label(self.ventana, image=self.foto)

        self.campos = [StringVar() for _ in range(3)]
        posicion = 10
        for campo in self.campos:
            label = Label(self.ventana, textvariable=campo, background='White', foreground='Black', font='arial 42 bold')
            label.place(x=posicion, y=100, width=100, height=100)
            posicion += 110

        self.ventana.mainloop()

    def generar_numero(self):
        return random.randint(0,9)

    def jugar(self):
        hay_siete = False
        for i in range(3):
            valor = self.generar_numero()
            self.campos[i].set(valor)
            if valor == 7:
                hay_siete = True

        if hay_siete:
            self.gano.pack(side=BOTTOM)
        else:
            self.gano.pack_forget()


if __name__ == "__main__":
    jugar = SieteAfortunado()
