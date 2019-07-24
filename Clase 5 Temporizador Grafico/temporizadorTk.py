from unidadTiempo import *
from Tkinter import *
from temporizador import *
from threading import *
from time import sleep

class InterfazTemporizador(Thread):
	def __init__(self):
		self.root = Tk()
		self.temporizador = Temporizador()
		self.frame = Frame(self.root)
		self.frame.pack()
		
		#variable de tipo String de Tk para almacenar un string
		self.inicio = StringVar()
		self.inicio.set("00 : 00 : 00")
		#se crea un ENTRY: caja de texto para capturar el valor
		self.text = Entry(self.frame, textvariable=self.inicio)
		self.text.pack(side=TOP)
		
		#variable de tipo string para almacenar el valor del 
		#temporizador
		self.tiempo = StringVar()
		
		#LABEL que mostrara el valor del temporizador
		self.display = Label(self.frame, textvariable = self.tiempo)
		self.display.pack(side=TOP)
		
		#se crea un boton para controlar el temporizador
		self.btnIniciar = Button(self.frame, text="Iniciar/Parar")
		#el bind me permite asociar el evento del objeto a traves
		#de una etiqueta
		#self.btnIniciar.bind("etiqueta", funcion)
		self.btnIniciar.bind("<Button-1>", self.cambiar)
		self.btnIniciar.pack(side=LEFT)
		
		self.btnEstablecer = Button(self.frame, text="Establecer")
		self.btnEstablecer.bind("<Button-1>", self.establecer)
		self.btnEstablecer.pack(side=RIGHT)
		
		Thread.__init__(self)
		self.start()
		
		self.root.mainloop()
	
	def cambiar(self, event):
		self.temporizador.detenido = not self.temporizador.detenido
	
	def establecer(self, event):
		try:
			lista = [int(x) for x in self.inicio.get().split(" : ")]
		except:
			self.inicio.set("00 : 00 : 00")
			lista = [0, 0, 0]
		
		self.temporizador.iniciar(lista)
	
	def run(self):
		while True:
			if not self.temporizador.detenido:
				self.temporizador.retroceder()
			
			sleep(0.5)
			self.tiempo.set(self.temporizador.mostrar_tiempo())

app = InterfazTemporizador()