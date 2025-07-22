from tkinter import *

#libreria basica
raiz = Tk()

#cambiar el titulo de la ventana
raiz.title("ventana .exe")

#tamaño de la ventana el primero es el ancho y el segundo es el alto
#si usamos false como variable no se puede modificar el tamaño de la ventana
raiz.resizable(True,True)


#cambiar icono de la ventana se copia la ruta relativa dando click derecho en la imagen
raiz.iconbitmap("interfazGrafica\icono.ico")

#cambiar el tamaño de la ventana
raiz.geometry("650x350")

#cambiar color del fondo bg es de back graoun
raiz.config(bg="black")



#Metemos raiz en un loop parar poder ver nuestra ventana
#siempre deve ir al final el loop
raiz.mainloop()