from tkinter import *

raiz = Tk()

mi_frame = Frame(raiz, width=800, height=400)
mi_frame.pack()


cuadroTexto = Entry(mi_frame)
cuadroTexto.grid(row=0, column=1)

nombreLabel = Label(mi_frame, text="Nombre ")
nombreLabel.grid(row=0, column=0)


raiz.mainloop()