from Mazo import Mazo
from Jugador import Jugador
from JugadorVirtual import JugadorVirtual

class Repartidor:

	def __init__(self, lista_jugadores):
		self.jugadores = lista_jugadores
		self.resultados = []
		self.mazo = Mazo()

	def repartir_cartas(self):
		for jugador in self.jugadores:
			cartas = [self.mazo.obtener_siguiente_carta(), self.mazo.obtener_siguiente_carta()]
			jugador.asignar_cartas(cartas)


	def jugar(self):
		ganador = 0
		valor = 0
		self.mazo.revolver()
		self.repartir_cartas()
		print('Juego iniciado hay:', len(self.jugadores))
		for i in range(len(self.jugadores)):
			suma = self.jugadores[i].jugar(self.mazo)
			resultado = 21 - suma
			if ((resultado > valor and resultado < 0) or (resultado == valor and 
				len(self.jugadores[i].cartas) < len(self.jugadores[ganador].cartas))):
				valor = resultado
				ganador = i
			print('La suma de',i,'es', suma)

			self.resultados.append(resultado)

		print('Los resultados son', self.resultados, self.jugadores[ganador].nombre, str(valor))

	def iniciar_juego(self):
		self.mazo.revolver()
		self.repartir_cartas()
		return {
			"j1": self.jugadores[0].cartas,
			"jv": self.jugadores[1].cartas
		}

	def determinar_ganador(self):
		ganador =0
		valor = 21
		for i in range(len(self.jugadores)):
			suma = self.jugadores[i].sumar_cartas()
			resultado = 21 - suma
			if(resultado < valor and resultado >= 0):
				valor = resultado
				ganador = i

		return ganador == 0

if(__name__ == "__main__"):
	j1 = Jugador('Jugador 1')
	j2 = JugadorVirtual('Computadora 1')
	repartidor = Repartidor([j1,j2])
	repartidor.jugar()

