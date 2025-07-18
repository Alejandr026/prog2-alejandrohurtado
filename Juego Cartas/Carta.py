

class Carta:

	def __init__(self, numero, palo):
		self.palo = palo
		self.numero = numero

	def imprimir(self):
		numero = self.convertir_numero_a_letras()
		print(numero, "de" , self.palo)

	@property
	def numero(self):
		print("Estamos en el getter")
		return 10 if self._numero > 10 else self._numero

	@numero.setter
	def numero(self, numero):
		if(numero >=1 and numero <= 13):
			self._numero = numero
		else:
			print("El numero es invalido")
	
	def convertir_numero_a_letras(self):
		valor = ""

		if (self.numero == 11):
			valor = "J"
		elif(self.numero == 12):
			valor = "Q"
		elif(self.numero == 13):
			valor = "K"
		elif(self.numero == 1):
			valor = "A"
		else:
			valor = str(self.numero)

		return valor

	def obtener_numero(self):
		return 10 if self.numero > 10 else self.numero

	def obtener_nombre_archivo(self):
		return "Cartas/"+self.convertir_numero_a_letras()+"_de_"+self.palo+".png"

def main():
	carta = Carta(11, "Tréboles")
	carta.numero = 14
	carta.imprimir()

	carta = Carta(12, "Tréboles")
	carta.imprimir()

	carta = Carta(13, "Tréboles")
	carta.imprimir()

	carta = Carta(1, "Tréboles")
	carta.imprimir()

	carta = Carta(8, "Tréboles")
	carta.imprimir()

if __name__ == "__main__":
	main()