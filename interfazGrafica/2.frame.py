from tkinter import *

raiz = Tk()
raiz.title("ventana .exe")
raiz.resizable(True,True)
raiz.iconbitmap("interfazGrafica\icono.ico")
#raiz.geometry("650x350")
raiz.config(bg="black")
#lo anterior esta explicado en el otro archivo

#Defenimos la varaible frame 
miFrame = Frame()
# se usa para posicionar widgets (como botones, etiquetas, cuadros de texto, etc.) 
# dentro de una ventana o contenedor.
#la n le dice que se vaya al norte 
#miFrame.pack(side="left", anchor="n")

#Se configura el frame para que se expanda automaticamente con la ventana se usan ejes x , y, both
miFrame.pack(fill="x" , expand= "True")
#ponemos el color que queremos que tenga y luego definimos su tamaño
miFrame.config(bg="red")
miFrame.config(width="650", height="350")

#configurar los bordes de nuestro frame, busca en google para mas ejemplos
miFrame.config(bd=35)
miFrame.config(relief="groove")

#configurar el tipo de raton que aparece en la ventana
miFrame.config(cursor="hand2")

raiz.mainloop()