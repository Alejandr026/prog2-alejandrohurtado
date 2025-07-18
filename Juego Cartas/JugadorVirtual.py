# Debe contener las cartas (instancias)
# Tener la capacidad de solicitar cartas (jugar)
# Imprimir sus cartas
# Poder sumar el valor de las cartas

from Interfaz import Interfaz
from Mazo import Mazo
from Jugador import Jugador

class JugadorVirtual(Jugador):

	def imprimir_juego(self):
		cartas = ['_']
		for i in range(1, len(self.cartas)):
			cartas.append(self.cartas[i].numero)

		print(cartas)

	def jugar(self, mazo):
		
		while(self.sumar_cartas() < 16):
			self.cartas.append(mazo.obtener_siguiente_carta())

		self.imprimir_juego()
		return self.sumar_cartas()



if __name__ == "__main__":
	mazo = Mazo()
	jugador1 = JugadorVirtual("Juan")
	print(jugador1.jugar(mazo))

