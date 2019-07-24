from unidadTiempo import *

class Temporizador:
	def __init__(self):
		self.hora = Hora()
		self.minuto = Minuto()
		self.segundo = Segundo()
		self.detenido = True
	
	def iniciar(self, tiempo):
		self.hora.iniciar(tiempo[0])
		self.minuto.iniciar(tiempo[1])
		self.segundo.iniciar(tiempo[2])
	
	def retroceder(self):
		self.segundo.retroceder()
		
		if self.segundo.valor == self.segundo.tope:
			self.minuto.retroceder()
		
			if self.minuto.valor == self.minuto.tope:
				self.hora.retroceder()
				"""
				if self.hora.valor == self.hora.tope:
					hora = 0
					minuto = 0
					segundo = 0

					self.reiniciar([hora,
									minuto,
									segundo])
				"""
		print str(self.hora.valor) + "h:" + str(self.minuto.valor) + "m:" + str(self.segundo.valor) + "s"
	
	def mostrar_tiempo(self):
		return str(self.hora.mostrarValor()) + " : " + str(self.minuto.mostrarValor()) + " : " + str(self.segundo.mostrarValor())
	
	def reiniciar(self, tiempo):
		self.hora.iniciar(tiempo[0])
		self.minuto.iniciar(tiempo[1])
		self.segundo.iniciar(tiempo[2])