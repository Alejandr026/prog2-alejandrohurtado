#!usr/bin/env python
# -*- coding: utf-8 -*-

class LectorDeArchivos:

	def __init__(self,nombre_archivo):
		try:
			self.lector = open(nombre_archivo, 'r', encoding='utf-8')
			self.esta_abierto = True
		except FileNotFoundException as error:
			self.lector = None
			self.esta_abierto = False
			print("No se encuentra el archivo llamado", nombre_archivo)

	def leer_linea(self):
		linea = None
		if (self.esta_abierto and not self.lector.closed):
			linea = self.lector.readline()
		return linea

	def leer_archivo_version2(self):
		archivo = None
		if (self.esta_abierto and not self.lector.closed):
			archivo = ""
			linea = self.lector.readline()
			while(len(linea) != 0):
				archivo += linea
				linea = self.lector.readline()

		return archivo

	def leer_archivo(self):
		archivo = None
		if (self.esta_abierto and not self.lector.closed):
			archivo = self.lector.readlines()

		return archivo


	def cerrar(self):
		if(self.esta_abierto):
			self.lector.close()


def main():
	lector = LectorDeArchivos("LectorDeArchivos.py")
	#print(lector.leer_linea())
	#print(lector.leer_linea())
	print(lector.leer_archivo_version2())
	lector.cerrar()


if __name__ == "__main__":
	main()