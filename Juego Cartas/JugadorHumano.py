# Debe contener las cartas (instancias)
# Tener la capacidad de solicitar cartas (jugar)
# Imprimir sus cartas
# Poder sumar el valor de las cartas

from Interfaz import Interfaz
from Mazo import Mazo
from Jugador import Jugador

class JugadorHumano(Jugador):
 
	def solicitar_carta(self, mazo):
		self.cartas.append(mazo.obtener_siguiente_carta())
		return self.sumar_cartas()

	def jugar(self, mazo):
		interfaz = Interfaz()
		solicitar = True
		titulo = "Digite:\n1- Pedir Carta\n2- Quedarse\nValor:"

		while(solicitar and self.sumar_cartas() <= 21):
			self.imprimir()
			valor = interfaz.solicitar_numero_entero(titulo)
			if (valor == 1):
				self.cartas.append(mazo.obtener_siguiente_carta())
				self.cartas[-1].imprimir()
			elif(valor == 2):
				solicitar = False

		return self.sumar_cartas()

if __name__ == "__main__":
	mazo = Mazo()
	jugador1 = JugadorHumano("Juan")
	print(jugador1.jugar(mazo))

