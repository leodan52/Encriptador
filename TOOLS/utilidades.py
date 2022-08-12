# Descripcion

import os

def AquiEstoy():
	return os.path.dirname(os.path.abspath(__file__))

def reescribir(ruta,nuevas_lineas):
	
	salida = open(ruta, "w")
	
	for i in nuevas_lineas:
		print(i,file=salida)
		
	salida.close()

def extraer(ruta):
	
	entrada = open(ruta, "r")
	Lista = []
	
	for i in entrada:
		if i.strip() == "":
			continue
			
		Lista.append(i.strip())
	
	entrada.close()
	return Lista


def lista2str(Lista):
	return "".join(Lista).replace("\n","")

def extraer_(ruta):
	
	n = ""
	
	while n == "":
		try:
			lineas = extraer(ruta)
			if lineas == []:
				print("Error.", ruta, " está vacia. Favor de llenarlo")
			else:
				return lista2str(lineas)
		except FileNotFoundError:
			print("Error,", ruta, "no existe")
		except IsADirectoryError:
			print("Error.", ruta, "es un directorio.")
		except UnicodeDecodeError:
			print("Error. No es un archivo válido.")
		except:
			print("Error desconocido")
			
		print("Corrigue tu archivo", ruta, "y oprime enter. ", end="")
		getpass("")
		
		
class RutasLlave:
	
	def __init__(self, r = []):
		self.rutas_lista = r.copy()
		self.ruta = AquiEstoy().replace("TOOLS", "") + "Lista_rutas.txt"
				
		self.CrearArchivoRutas()
		
		self.Extraer()
		
	def CrearArchivoRutas(self):
		entrada = open(self.ruta, "w")
		for i in self.rutas_lista:
			print(i.strip(), file=entrada)
		entrada.close()	
		
	def EliminarArchivoRutas(self):
		os.remove(self.ruta)
		
	def Extraer(self):
		
		lineas = open(self.ruta, "r")
		
		self.KEY = ""
		
		for linea in lineas:
			self.KEY = self.KEY + extraer_(linea.strip())
		
		
