# Descripcion

import TOOLS.utilidades as ut
from getpass import getpass

class Encriptador:
	
	def __init__(self, archivo, clase_llaves):
		self.key = clase_llaves.KEY
		self.LLAVES = clase_llaves
		self.ruta_ctrs = archivo
		self.Ruta_caract = ut.AquiEstoy() + "/.carac.txt"
		self.caracteres = "".join(ut.extraer(self.Ruta_caract))
		
		self.ActualizarDicc()
		
	def ActualizarDicc(self):
		cadena = self.key
		
		nueva = self.caracteres
		
		for i in self.caracteres:
			cadena.replace(i,"")
			
		for j in cadena:
			if j not in nueva:
				nueva = nueva + j
		
		if nueva != self.caracteres:
			ut.reescribir(self.Ruta_caract, [self.caracteres])
		
	def encriptador(self):
		contrasenas = ut.extraer(self.ruta_ctrs)
		listas = self.EncriptarLista(contrasenas)
		
		if listas[0]:
			pass
		else:
			return listas
		
		if contrasenas != listas:
			ut.reescribir(self.ruta_ctrs,listas)
			
		return [True]
		
	def EncriptarLista(self, lineas):
		
		salida = []	
		
		loop = ""
		
		while loop == "":
		
			loop = "s"
				
			for linea in lineas:
				
				if linea[0] == "*":
					salida.append(linea)
					continue
					
				try:
					salida.append("*:" + self.encriptar(linea))
				except ValueError:
					mensaje = [False,"Llaves insuficientes.\n Agregue todas las llaves necesarias."]
					return mensaje
					self.LLAVES.extraer()
					loop = ""
					break
		return salida			
	
	def encriptar2(self,linea):	
		salida = []
		
		for letra in linea:
			n = self.key.index(letra)
			salida.append(str(n))
			
		return ":".join(salida)
	
	def LlaveMaestra(self):
		llave = ""
		
		for i in self.key:
			if i not in llave:
				llave = llave + i
		
		return llave
		
	def encriptar(self,linea):	
		
		salida = []
		
		llave = self.LlaveMaestra()
		
		for letra in linea:
			n = llave.index(letra)
			salida.append(str(n))
		
		return ":".join(salida)
			
	def Desencriptador(self, n=1):
		listas = self.EncriptarLista(ut.extraer(self.ruta_ctrs))
		
		if listas[0]:
			pass
		else:
			return listas
		
		new_listas = []
		
		llave = self.LlaveMaestra()
		
		for linea in listas:
			password = ""
			linea = linea.replace("*:","").split(":")
			
			for i in linea:
				if i == "":
					continue
				i = int(i)
				if n == 1:
					password = password + llave[i]
				else:
					password = password + self.key[i]
			new_listas.append(password)
			
		ut.reescribir(self.ruta_ctrs,new_listas)
		
		return [True]
