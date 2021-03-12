# -*-encoding:utf8-*-
import sys

import ImgMus
import data.main as main
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QTreeWidgetItem, QDialog

import m

archivos = main.Definir()
buscar = main.Buscadores()
xml = main.XML()
nombres = main.Archivos()
listass = ["video9.mp4"]
A = "xxxx1.mp4"

class Editar(QDialog):
    def __init__(self, arch):
        self.arch = arch
        QDialog.__init__(self)
        uic.loadUi("d_editar.ui", self)
        self.setWindowTitle(arch)
        for item in archivos.todos():
            archivo = [buscar.bus_nombre(item)[0], buscar.bus_nombre(item)[2], buscar.bus_nombre(item)[1], buscar.bus_nombre(item)[4], buscar.bus_nombre(item)[3]]
            if any(arch in s for s in archivo):
                self.lin_autor.setText(buscar.bus_nombre(item)[2])
                self.lin_genero.setText(buscar.bus_nombre(item)[1])
                self.lin_fecha.setText(buscar.bus_nombre(item)[4])
                self.lin_album.setText(buscar.bus_nombre(item)[3])
        self.b_editar.clicked.connect(self.cambiar)

    def cambiar(self):
        xml.editar(self.arch, "interprete", self.lin_autor.text())
        xml.editar(self.arch, "genero", self.lin_genero.text())
        xml.editar(self.arch, "fecha", self.lin_fecha.text())
        xml.editar(self.arch, "album", self.lin_album.text())
        self.close()


class Lista(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        global listass
        uic.loadUi("d_lista.ui", self)
        self.setWindowTitle("LISTAS")
        self.b_cancelar.clicked.connect(self.close)
        for i in xml.listas():
            self.cb_lista.addItem(i)
        self.cb_lista.activated.connect(self.refresh)
        self.b_crear.clicked.connect(self.crea)
        self.b_eliminar.clicked.connect(self.eli)
        self.b_agregar.clicked.connect(self.elemento)
        self.b_quitar.clicked.connect(self.eli_elemento)
        self.b_seleccionar.clicked.connect(self.selec)

    def refresh(self):
        self.t_lista.clear()
        cont = ["",]
        for i in xml.lis_list(self.cb_lista.currentText()):
            cont[0] = i
            self.t_lista.insertTopLevelItems(0, [QTreeWidgetItem(self.t_lista, cont)])

        self.t_todo.clear()
        cont = ["",]
        for i in archivos.todos():
            cont[0] = i
            self.t_todo.insertTopLevelItems(0, [QTreeWidgetItem(self.t_todo, cont)])

    def elemento(self):
        xml.cre_cancion(self.cb_lista.currentText(), self.t_todo.currentItem().text(0))
        self.refresh()

    def eli_elemento(self):
        xml.eli_cancion(self.cb_lista.currentText(), self.t_lista.currentItem().text(0))
        self.refresh()

    def crea(self):
        xml.cre_list(self.lin_crear.text())
        self.cb_lista.addItem(self.lin_crear.text())
        self.lin_crear.clear()

    def eli(self):
        xml.eli_list(self.cb_lista.currentText())
        self.cb_lista.removeItem(self.cb_lista.currentIndex())

    def selec(self):
        global listass
        objeto = Ventana()
        listass = xml.lis_list(self.cb_lista.currentText())
        self.close()


class Agregar(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi("d_agregar.ui", self)
        self.setWindowTitle("LISTAS")
        self.b_cancelar.clicked.connect(self.close)
        archivo = ["",]
        for i in range(0, len(nombres.listar())):
            archivo[0] = nombres.listar()[i]
            self.t_lista_a.insertTopLevelItems(0, [QTreeWidgetItem(self.t_lista_a, archivo)])
        self.b_agregar.clicked.connect(self.agrega)

    def abrireditar(self):
        if self.t_lista_a.currentItem():
            arch = self.t_lista_a.currentItem().text(0)
            #crear el objeto
            self.dialogo = Editar(arch)
            self.dialogo.exec_()
        else:
            self.abrirerror()

    def agrega(self):
        arch = self.t_lista_a.currentItem().text(0)
        nombres.agregar(arch)
        xml.actualizar()
        self.abrireditar()
        self.close()



class Error(QDialog):
    def __init__(self):
        #self.err = err
        QDialog.__init__(self)
        uic.loadUi("d_error.ui", self)
        self.setWindowTitle("ERROR")
        #self.lab_error.setText(err)


class Ventana(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self) # Iniciar el objeto
        global lista
        uic.loadUi("Reproductor.ui", self)
        self.listar()
        global A
        self.b_buscar.clicked.connect(self.busca)
        self.l_buscar.returnPressed.connect(self.busca)
        self.b_editar.clicked.connect(self.abrireditar)
        self.b_editar.clicked.connect(self.lista.clear)
        self.b_editar.clicked.connect(self.listar)
        self.b_filtro.clicked.connect(self.listar)
        self.b_lista.clicked.connect(self.abrirlista)
        self.b_lista.clicked.connect(self.li_lista)
        self.b_agregar.clicked.connect(self.abriragregar)
        self.b_agregar.clicked.connect(self.listar)
        self.b_reproducir.clicked.connect(self.capturarname)
        self.b_reproducir.clicked.connect(self.reproducir)
        self.b_eliminar.clicked.connect(self.elimin)
        self.b_eliminar.clicked.connect(self.listar)
        self.b_eliminar.clicked.connect(self.abrirerror)

    def elimin(self):
        if self.lista.currentItem():
            arch = self.lista.currentItem().text(0)
            nombres.eliminar(arch)
        else:
            pass

    def li_lista(self):
        global lista
        self.lista.clear()
        for item in listass:
            nom = item
            print(buscar.bus_nombre(nom)[0])
            archivo = [buscar.bus_nombre(nom)[0], buscar.bus_nombre(nom)[2], buscar.bus_nombre(nom)[1],
                       buscar.bus_nombre(nom)[4], buscar.bus_nombre(nom)[3]]
            self.lista.insertTopLevelItems(1, [QTreeWidgetItem(self.lista, archivo)])


    def listar(self):
        self.lista.clear()
        if self.r_todo.isChecked():
            for item in archivos.todos():
                nom = item
                archivo = [buscar.bus_nombre(nom)[0], buscar.bus_nombre(nom)[2], buscar.bus_nombre(nom)[1], buscar.bus_nombre(nom)[4], buscar.bus_nombre(nom)[3]]
                self.lista.insertTopLevelItems(1, [QTreeWidgetItem(self.lista, archivo)])
        if self.r_video.isChecked():
            for item in archivos.videos():
                nom = item
                archivo = [buscar.bus_nombre(nom)[0], buscar.bus_nombre(nom)[2], buscar.bus_nombre(nom)[1], buscar.bus_nombre(nom)[4], buscar.bus_nombre(nom)[3]]
                self.lista.insertTopLevelItems(0, [QTreeWidgetItem(self.lista, archivo)])
        if self.r_musica.isChecked():
            for item in archivos.musica():
                nom = item
                archivo = [buscar.bus_nombre(nom)[0], buscar.bus_nombre(nom)[2], buscar.bus_nombre(nom)[1], buscar.bus_nombre(nom)[4], buscar.bus_nombre(nom)[3]]
                self.lista.insertTopLevelItems(0, [QTreeWidgetItem(self.lista, archivo)])
        if self.r_imagen.isChecked():
            for item in archivos.fotos():
                nom = item
                archivo = [buscar.bus_nombre(nom)[0], buscar.bus_nombre(nom)[2], buscar.bus_nombre(nom)[1], buscar.bus_nombre(nom)[4], buscar.bus_nombre(nom)[3]]
                self.lista.insertTopLevelItems(0, [QTreeWidgetItem(self.lista, archivo)])

    def busca(self):
        self.lista.clear()
        archivo = []
        nom = self.l_buscar.text()
        for item in archivos.todos():
            archivo = [buscar.bus_nombre(item)[0], buscar.bus_nombre(item)[2], buscar.bus_nombre(item)[1], buscar.bus_nombre(item)[4], buscar.bus_nombre(item)[3]]
            if any(nom.upper() in s for s in archivo) or any(nom.lower() in s for s in archivo):
                self.lista.insertTopLevelItems(0, [QTreeWidgetItem(self.lista, archivo)])


    def abrirerror(self):
        #self.err = err
        self.dialogo = Error()
        self.dialogo.exec_()

    def abrirlista(self):
        self.dialogo = Lista()
        self.dialogo.exec_()

    def abriragregar(self):
        self.dialogo = Agregar()
        self.dialogo.exec_()

    def capturarname(self):
        arch = self.lista.currentItem().text(0)
        return arch


    def abrireditar(self):
        if self.lista.currentItem():
            arch = self.lista.currentItem().text(0)
            #crear el objeto
            self.dialogo = Editar(arch)
            self.dialogo.exec_()
        else:
            self.abrirerror()
            return arch

    def reproducir(self):
        s = self.capturarname()
        defi=main.Definir()
        print(s)
        if s in defi.videos() or defi.musica():
            player.mostrar(s)
        if s in defi.fotos():
            ImgMus.reproducirImagenes(s)










# Instanciar la aplicación
app = QApplication(sys.argv)
# Crear el objeto de la aplicaciòn
reproductor = Ventana()

player = m.VideoPlayer(A)
player.setWindowTitle("Player")
player.resize(600, 400)
# Mostrar la ventana
reproductor.show()
# Ejecutar el reproductor
sys.exit(app.exec_())