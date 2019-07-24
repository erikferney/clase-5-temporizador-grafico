from temporizador import *
from time import sleep

hora = 0
minuto = 1
segundo = 0

tempo = Temporizador()
tempo.iniciar([hora, minuto, segundo])

rango = (hora * 60 * 60) + (minuto * 60) + segundo

for ln in range(rango):
	tempo.retroceder()
	print tempo.mostrar_tiempo()
	#sleep(0.5)
