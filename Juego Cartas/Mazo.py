#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Carta import Carta
import random

class Mazo:

	def __init__(self):
		self.cartas = []
		self.ultima_repartida = 0
		self.crear_mazo()

	def crear_mazo(self):
		self.ultima_repartida = 0
		simbolos = [ "Treboles", "Diamantes", "Corazones", "Espadas" ]
		for j in range(0,4):
			for i in range(1,14):
				carta = Carta(i, simbolos[j])
				self.cartas.append(carta)

	def revolver(self):
		for celda in range(len(self.cartas)):
			aleatorio = random.randint(0,51)
			(self.cartas[celda], self.cartas[aleatorio]) = (self.cartas[aleatorio], self.cartas[celda])


	def imprimir(self):
		for instanciaCarta in self.cartas:
			instanciaCarta.imprimir()


	def obtener_siguiente_carta(self):
		carta = self.cartas[self.ultima_repartida]
		self.ultima_repartida += 1
		return carta

if __name__ == "__main__":		
	mazo1 = Mazo()
	mazo1.imprimir()
	print(":::::::::::::::::::")
	mazo1.obtener_siguiente_carta().imprimir()
	mazo1.obtener_siguiente_carta().imprimir()
	mazo1.revolver()
	mazo1.imprimir()
