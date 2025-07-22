from tkinter import *

raiz = Tk()
miFrame = Frame()
miFrame = Frame(raiz, width=500, height=400 )
miFrame.pack()

#le damos ex texto a mostrar de nuestra varaible
#miLabel = Label(miFrame, text="Hola mundo")
#definir la ubicasion de mi texto
#miLabel.place(x=250 , y= 200)

#se puede acortar el codigo asi y se le puede añadir fg =color de letra, font = fuente de letra
Label(miFrame, text="Hola mundo", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

#Agremar imagenes 
mi_imagen=PhotoImage(file="interfazGrafica\perfilamarillo.png")
Label(miFrame, image=mi_imagen).place(x=100, y= 200)


raiz.mainloop()