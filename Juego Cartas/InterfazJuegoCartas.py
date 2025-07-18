
from tkinter import *
from Repartidor import Repartidor

from JugadorHumano import JugadorHumano
from JugadorVirtual import JugadorVirtual


class InterfazJuegoCartas:
 
	def __init__(self):
		self.ventana = Tk()
		self.ventana.geometry('1200x600')
		self.canvas = Canvas(self.ventana, width=1200, height=600)
		self.canvas.pack()
		self.dibujar_fondo()

		self.dibujar_etiquetas()

		self.btnIniciar = Button(self.ventana, text="Iniciar Juego", command=self.jugar)
		self.btnQuedarse = Button(self.ventana, text="Quedarse", command=self.finalizar_juego)
		self.btnSolicitar = Button(self.ventana, text="Solicitar Carta", command=self.solicitar_carta)
		self.ocultar_opciones_juego()

		self.j1 = JugadorHumano('Jugador 1')
		self.jv1 = JugadorVirtual('Compu 1')
		self.repartidor = Repartidor([self.j1, self.jv1])

		self.ventana.mainloop()

	def jugar(self):
		self.dibujar_fondo()
		self.jvx = 110
		self.jvy = 143
		self.j1x = 110
		self.j1y = 490
		self.jvx_inicio = self.jvx
		cartas = self.repartidor.iniciar_juego()
		self.jv1.jugar(self.repartidor.mazo)
		self.jvx = self.definir_estado_inicial(cartas["jv"], self.jvx, self.jvy, True)
		self.j1x = self.definir_estado_inicial(cartas["j1"], self.j1x, self.j1y)
		self.mostrar_opciones_juego()

	def solicitar_carta(self):
		suma = self.j1.solicitar_carta(self.repartidor.mazo)
		if (suma > 21):
			self.finalizar_juego()

		self.dibujar_rectangulos(1, self.j1x-60, 400,120,175,0)
		self.dibujar_carta(self.j1x, self.j1y,self.j1.cartas[-1].obtener_nombre_archivo())
		self.j1x += 125

	def finalizar_juego(self):
		self.dibujar_rectangulos(1,self.jvx_inicio-60, self.jvy-88, 120,175,0)
		self.dibujar_carta(self.jvx_inicio, self.jvy, self.jv1.cartas[0].obtener_nombre_archivo())

		ganadorHumano = self.repartidor.determinar_ganador()
		if(ganadorHumano):
			self.etiqueta_ganador.config(text="Gana el jugador")
		else:
			self.etiqueta_ganador['text'] = "La casa gana"

		self.ocultar_opciones_juego()


	def definir_estado_inicial(self, cartas, x,y , ocultar_primera = False):
		for i in range(len(cartas)):
			self.dibujar_rectangulos(1, x-60, y-88, 120, 175, 5)
			nombre = 'Cartas/_s.png' if ocultar_primera and i == 0 else cartas[i].obtener_nombre_archivo()
			self.dibujar_carta(x,y,nombre)
			x += 125
		return x


	def mostrar_opciones_juego(self):
		self.btnSolicitar.place(x=700, y=500)
		self.btnQuedarse.place(x=700, y=550)
		self.btnIniciar.place_forget()

	def ocultar_opciones_juego(self):
		self.btnIniciar.place(x=400, y=300)
		self.btnQuedarse.place_forget()
		self.btnSolicitar.place_forget()


	def dibujar_etiquetas(self):
		etiqueta = Label(self.ventana, text="Computadora 1", background="Green", foreground="White", font="arial 15 bold")
		etiqueta.place(x=50, y=20)
		etiqueta = Label(self.ventana, text="Jugador 1", background="Green", foreground="White", font="arial 15 bold")
		etiqueta.place(x=50, y=360)
		self.etiqueta_ganador = Label(self.ventana, text="", background="Green", foreground="White", font="arial 15 bold")
		self.etiqueta_ganador.place(x=50, y=280)

	def dibujar_rectangulos(self, cantidad, xInicio, yInicio, xTam, yTam, margen=10):
		for i in range(cantidad):
			self.dibujar_poligono([xInicio,xInicio+xTam,xInicio+xTam, xInicio],[yInicio, yInicio, yInicio+yTam, yInicio+yTam], fill='#FFFFFF', width=2, outline='#000000')
			xInicio = xInicio + xTam + margen

	def dibujar_poligono(self, x, y, **args):
		puntos = []
		for i in range(len(x)):
			puntos.append(x[i])
			puntos.append(y[i])

		puntos.append(x[0])
		puntos.append(y[0])

		return self.canvas.create_polygon(puntos,**args)		


	def dibujar_fondo(self):
		fondo = PhotoImage(file='juegoCartas/fondo.png')
		imagen = Label(image=fondo)
		imagen.image = fondo

		self.canvas.create_image(300,200, image=fondo)
		self.canvas.create_image(300,400, image=fondo)
		self.canvas.create_image(900,200, image=fondo)
		self.canvas.create_image(900,400, image=fondo)

		adornos = PhotoImage(file='juegoCartas/adornos.png')
		imagen = Label(image=adornos)
		adornos = adornos.subsample(7)
		imagen.image = adornos

		self.canvas.create_image(980,460, image=adornos)

	def dibujar_carta(self, x=110, y=143, imagen = 'juegoCartas/2_de_treboles.png'):
		imagen_canvas = PhotoImage(file=imagen)
		imagen_canvas = imagen_canvas.subsample(2)
		imagen_label = Label(image=imagen_canvas)
		imagen_label.image = imagen_canvas
		self.canvas.create_image(x,y, image=imagen_canvas)



def main():
	interfaz = InterfazJuegoCartas()

if __name__ == "__main__":
	main()