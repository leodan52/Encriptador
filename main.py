# Descripcion
from UI.ventana_encriptador_ui import *
from PyQt5.QtWidgets import QFileDialog
from TOOLS.encriptar import *

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self, *args, **kwargs):
		QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
		self.setupUi(self)
		self.Llaves = []
		
		self.accion = "Encriptar"
		self.Ejecutar.setText(self.accion)
		
		self.Explorador_1.clicked.connect(self.cuadro_1)
		self.Explorador_2.clicked.connect(self.cuadro_2)
		self.BorrarLlave.clicked.connect(self.BorrarLlave_)
		self.BorrarLlaves.clicked.connect(self.BorrarLlaves_)
		
		self.Agregar.clicked.connect(self.AgregarLlaves)
		
		self.Ejecutar.clicked.connect(self.EncriptarBoton)
		
	def EncriptarBoton(self):
		if self.Llaves == []:
			self.MensajeUsuario("No hay llaves")
			return
		if self.EntradaFile.text().strip() == "":
			self.MensajeUsuario("Elige un archivo a encriptar")
			return
			
		Rutas = ut.RutasLlave(self.Llaves)

		encriptador = Encriptador(self.EntradaFile.text().strip(),Rutas)
		
		if self.accion == "Encriptar":
			mensaje = encriptador.encriptador()
			if mensaje[0] == False:
				self.MensajeUsuario(mensaje[1])
				return
			self.MensajeUsuario("Archivo encriptado")
			self.accion = "Desencriptar"
		else:
			mensaje = encriptador.Desencriptador()
			if mensaje[0] == False:
				self.MensajeUsuario(mensaje[1])
				return
			self.MensajeUsuario("Archivo desencriptado.\n Revise su archivo.\n Recomendamos que lo vuelva\n a encriptar a la brevedad")
			self.accion = "Encriptar"
		
			
		self.Ejecutar.setText(self.accion)
		Rutas.EliminarArchivoRutas()
		
	def MensajeUsuario(self,mensaje):
		self.CuadroMensaje.setText(mensaje)
	
	def BorrarLlave_(self):
		try:
			index = self.ListaDeLlaves.currentRow()
			self.ListaDeLlaves.takeItem(index)
			self.RefrescarLista()
		except AttributeError:
			pass
		
	def BorrarLlaves_(self):
		self.ListaDeLlaves.clear()
	
	def AgregarLlaves(self):
		ruta = self.EntradaLlaves.text().strip()
		if ruta == "":
			self.MensajeUsuario("No hay llave")
		elif ruta not in self.Llaves:
			self.ListaDeLlaves.addItem(ruta)
		else:
			self.MensajeUsuario("Esa llaves ya está registrada")
		
		self.EntradaLlaves.setText("")
		self.RefrescarLista()
			
	def RefrescarLista(self):
		self.Llaves = []
		
		indice = self.ListaDeLlaves.count()
		
		for i in range(indice):
			self.Llaves.append(self.ListaDeLlaves.item(i).text())
	
	def cuadro_1(self):
		ruta = self.Explorar_files()
		self.EntradaFile.setText(ruta)
	
	def cuadro_2(self):
		ruta = self.Explorar_files()
		self.EntradaLlaves.setText(ruta)
	
	def Explorar_files(self):
		return QFileDialog.getOpenFileName(self,"Abrir archivo", ".", "Archivo de texto (*.txt)")[0]
	
if __name__ == "__main__":
	app = QtWidgets.QApplication([])
	Ventana = MainWindow()
	Ventana.show()
	app.exec_()
