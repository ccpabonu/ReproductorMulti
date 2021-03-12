# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


import data.main as main
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

defin = main.Definir()
buscador1 = main.Buscadores()
xml1 = main.XML()
archivo1 = main.Archivos()
        
class Ui_Aviso(QMainWindow):
    def setupUi(self, Aviso):
        Aviso.setObjectName("Aviso")
        Aviso.resize(352, 149)
        self.centralwidget = QtWidgets.QWidget(Aviso)
        self.centralwidget.setObjectName("centralwidget")
        self.Ops = QtWidgets.QLabel(self.centralwidget)
        self.Ops.setGeometry(QtCore.QRect(0, 20, 341, 81))
        self.Ops.setObjectName("Ops")
        self.orden = QtWidgets.QLabel(self.centralwidget)
        self.orden.setGeometry(QtCore.QRect(30, 100, 291, 31))
        self.orden.setObjectName("orden")
        Aviso.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Aviso)
        self.statusbar.setObjectName("statusbar")
        Aviso.setStatusBar(self.statusbar)

        self.retranslateUi(Aviso)
        QtCore.QMetaObject.connectSlotsByName(Aviso)

    def retranslateUi(self, Aviso):
        _translate = QtCore.QCoreApplication.translate
        Aviso.setWindowTitle(_translate("Aviso", "MainWindow"))
        self.Ops.setText(_translate("Aviso", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">ARCHIVO NO ENCONTRADO</span></p><p align=\"center\"><span style=\" font-size:14pt;\">REINTENTE</span></p></body></html>"))
        self.orden.setText(_translate("Aviso", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt;\">(Cierre para reintentar)</span></p></body></html>"))


class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 540)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(40, 80, 171, 31))
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(4)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(249, 95, 383, 391))
        self.textEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setText("")
        self.textEdit.setReadOnly(True)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 160, 161, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 250, 161, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 340, 161, 51))
        self.pushButton_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(250, 60, 381, 41))
        self.label_2.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 127);")
        self.label_2.setObjectName("label_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(40, 430, 161, 51))
        self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 661, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(42, 50, 171, 21))
        self.label_4.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.MuestraMusica)
        self.pushButton_2.clicked.connect(self.MuestraVideo)
        self.pushButton_3.clicked.connect(self.MuestraImagenes)
        self.pushButton_4.clicked.connect(self.Accion)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setCurrentText(_translate("MainWindow", "EDITAR"))
        self.comboBox.setItemText(0, _translate("MainWindow", "EDITAR"))
        self.comboBox.setItemText(1, _translate("MainWindow", "AGREGAR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ORDENAR"))
        self.comboBox.setItemText(3, _translate("MainWindow", "LISTAS"))
        self.pushButton.setText(_translate("MainWindow", "MUSICA"))
        self.pushButton_2.setText(_translate("MainWindow", "VIDEOS"))
        self.pushButton_3.setText(_translate("MainWindow", "IMAGENES"))
        self.label_2.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INTRODUZCA EL NOMBRE DEL</span></p><p align=\"center\"><span style=\" font-weight:600;\">ARCHIVO QUE DESEA AGREGAR</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ARCHIVOS ENCONTRADOS PARA EDITAR</p></body></html>"))
        self.pushButton_4.setText(_translate("MainWindow", "VER O EDITAR INFO."))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">¡BIENVENIDO!</span></p></body></html>"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INTRODUZCA EL NOMBRE DEL</span></p><p align=\"center\"><span style=\" font-weight:600;\">ARCHIVO QUE DESEA AGREGAR</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">ESCOGA UNA ACCION:</p></body></html>"))
        self.pushButton_5.setText(_translate("MainWindow", "VER O EDITAR INFO."))
        
        self.comboBox.activated.connect(self.Arquimedes)
        

    def Arquimedes(self):
        item = self.comboBox.currentText()
        if item == "EDITAR":
            self.textEdit.setText("PULSE EL TIPO DE ARCHIVO QUE DESEA OPERAR")
            self.pushButton.clicked.connect(self.MuestraMusica)
            self.pushButton_2.clicked.connect(self.MuestraVideo)
            self.pushButton_3.clicked.connect(self.MuestraImagenes)
            self.pushButton_4.clicked.connect(self.Accion)
            self.label_2.setText("<html><head/><body><p align=\"center\">ARCHIVOS ENCONTRADOS PARA EDITAR</p></body></html>")
            self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.pushButton.setGeometry(QtCore.QRect(40, 160, 161, 51))
            self.pushButton_2.setGeometry(QtCore.QRect(40, 250, 161, 51))
            self.pushButton_3.setGeometry(QtCore.QRect(40, 340, 161, 51))
            self.pushButton.setText("MUSICA")
            self.pushButton_2.setText("VIDEOS")
            self.pushButton_3.setText("IMAGENES")
            self.pushButton_4.setText("VER O EDITAR INFO.")
            self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
            
        elif item == "AGREGAR":
            #self.textEdit.setText("Ahora agregamos")
            self.label_2.setText("<html><head/><body><p align=\"center\">ARCHIVOS ENCONTRADOS PARA AGREGAR</p></body></html>")
            self.pushButton.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.pushButton_3.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.pushButton_4.setText("INSERTAR DATOS")
            self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.pushButton_4.clicked.connect(self.agrega)
            

            if not archivo1.listar():
                self.textEdit.setText("<html><head/><body><p><span style=\" color:#ff0000;\">NO HAY POSIBLES ARCHIVOS PARA AGREGAR </span></p><p><span style=\" color:#ff0000;\"></span></p></body></html>")
            else:
                ii = ""
                lon = len(archivo1.listar())
                for j in archivo1.listar():
                    ii += (j)
                    ii += '\n' + "" + '\n'
                    lon -= 1
                    if lon < 0:
                        break
                self.textEdit.setText(ii)
                    
        elif item == "ORDENAR":
            self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
            self.pushButton.setGeometry(QtCore.QRect(40, 160, 161, 51))
            self.pushButton_2.setGeometry(QtCore.QRect(40, 250, 161, 51))
            self.pushButton_3.setGeometry(QtCore.QRect(40, 340, 161, 51))
            self.label_2.setText("<html><head/><body><p align=\"center\">LISTA ORDENADA</p></body></html>")
            self.pushButton.setText("POR INTERPRETE")
            self.pushButton_2.setText("POR FECHA")
            self.pushButton_3.setText("POR ALBUM")
            self.pushButton_4.setText("POR GENERO")
            self.pushButton_5.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.textEdit.setText("Ordenamos")
            
        else:
            self.textEdit.setText("ESCOGA EL TIPO DE ARCHIVO")
            self.label_2.setText("<html><head/><body><p align=\"center\">LISTAS DE REPRODUCCION</p></body></html>")
            self.pushButton.setText("MUSICA")
            self.pushButton.setGeometry(QtCore.QRect(40, 140, 161, 51))
            self.pushButton_2.setText("VIDEOS")
            self.pushButton_2.setGeometry(QtCore.QRect(40, 210, 161, 51))
            self.pushButton_3.setText("IMAGENES")
            self.pushButton_3.setGeometry(QtCore.QRect(40, 280, 161, 51))
            self.pushButton_4.setText("VER Y EDITAR LISTA")
            self.pushButton_4.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.pushButton_5.setGeometry(QtCore.QRect(40, 370, 161, 51))
            self.pushButton_5.setStyleSheet("background-color: rgb(255, 255, 127);")
            self.pushButton_5.setObjectName("pushButton_5")
            self.pushButton_5.setText("CREAR LISTA")

            self.pushButton.clicked.connect(self.ListM)
            self.pushButton_2.clicked.connect(self.ListV)
            self.pushButton_3.clicked.connect(self.ListI)
            self.pushButton_4.clicked.connect(self.ListS)
            self.pushButton_5.clicked.connect(self.ListC)            

            
            
    def ListM(self):
        self.textEdit.setText(pintarNom(xml1.listas(1)))

    def ListV(self):
        self.textEdit.setText(pintarNom(xml1.listas(0)))

    def ListI(self):
        self.textEdit.setText(pintarNom(xml1.listas(2)))

    def ListS(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_EditListas()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def ListC(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_CreaListas()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
            
        
    def MuestraMusica(self):    
        self.textEdit.setText(pintarNom(defin.musica()))

    def MuestraVideo(self):
        self.textEdit.setText(pintarNom(defin.videos()))

    def MuestraImagenes(self):
        self.textEdit.setText(pintarNom(defin.fotos()))
    
    def Accion(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_DetallesEditar()
        self.ui.setupUi(self.ventana)
        self.ventana.show()

    def agrega(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_VentAgregar()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
            
        #else:
            #self.ventana = QtWidgets.QMainWindow()
            #self.ui = Ui_Aviso()
            #self.ui.setupUi(self.ventana)
            #self.ventana.show()

##
class Ui_DetallesEditar(QMainWindow):

    def __init__(self,parent = None):
        super(Ui_DetallesEditar, self).__init__(parent)
        
    def setupUi(self, DetallesEditar):
        DetallesEditar.setObjectName("DetallesEditar")
        DetallesEditar.resize(621, 376)
        DetallesEditar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(DetallesEditar)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 50, 20, 231))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.LabAct = QtWidgets.QLabel(self.centralwidget)
        self.LabAct.setGeometry(QtCore.QRect(197, 20, 101, 21))
        self.LabAct.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.LabAct.setObjectName("LabAct")
        self.actualname = QtWidgets.QTextEdit(self.centralwidget)
        self.actualname.setGeometry(QtCore.QRect(136, 50, 211, 31))
        self.actualname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.actualname.setObjectName("actualname")
        self.actualname.setReadOnly(True)
        self.actualinterp = QtWidgets.QTextEdit(self.centralwidget)
        self.actualinterp.setGeometry(QtCore.QRect(136, 100, 211, 31))
        self.actualinterp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.actualinterp.setObjectName("actualinterp")
        self.actualinterp.setReadOnly(True)
        self.actualalbm = QtWidgets.QTextEdit(self.centralwidget)
        self.actualalbm.setGeometry(QtCore.QRect(136, 200, 211, 31))
        self.actualalbm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.actualalbm.setObjectName("actualalbm")
        self.actualalbm.setReadOnly(True)
        self.actualgen = QtWidgets.QTextEdit(self.centralwidget)
        self.actualgen.setGeometry(QtCore.QRect(136, 250, 211, 31))
        self.actualgen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.actualgen.setObjectName("actualgen")
        self.actualgen.setReadOnly(True)
        self.actualdate = QtWidgets.QTextEdit(self.centralwidget)
        self.actualdate.setGeometry(QtCore.QRect(136, 150, 211, 31))
        self.actualdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.actualdate.setObjectName("actualdate")
        self.actualdate.setReadOnly(True)
        self.newname = QtWidgets.QTextEdit(self.centralwidget)
        self.newname.setGeometry(QtCore.QRect(380, 50, 211, 31))
        self.newname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newname.setObjectName("newname")
        self.newdate = QtWidgets.QTextEdit(self.centralwidget)
        self.newdate.setGeometry(QtCore.QRect(380, 150, 211, 31))
        self.newdate.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newdate.setObjectName("newdate")
        self.newgen = QtWidgets.QTextEdit(self.centralwidget)
        self.newgen.setGeometry(QtCore.QRect(380, 250, 211, 31))
        self.newgen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newgen.setObjectName("newgen")
        self.newalbm = QtWidgets.QTextEdit(self.centralwidget)
        self.newalbm.setGeometry(QtCore.QRect(380, 200, 211, 31))
        self.newalbm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newalbm.setObjectName("newalbm")
        self.LabNew = QtWidgets.QLabel(self.centralwidget)
        self.LabNew.setGeometry(QtCore.QRect(441, 20, 101, 21))
        self.LabNew.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.LabNew.setObjectName("LabNew")
        self.newinterp = QtWidgets.QTextEdit(self.centralwidget)
        self.newinterp.setGeometry(QtCore.QRect(380, 100, 211, 31))
        self.newinterp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.newinterp.setObjectName("newinterp")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 50, 71, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabName = QtWidgets.QLabel(self.layoutWidget)
        self.LabName.setObjectName("LabName")
        self.verticalLayout.addWidget(self.LabName)
        self.LabInterp = QtWidgets.QLabel(self.layoutWidget)
        self.LabInterp.setObjectName("LabInterp")
        self.verticalLayout.addWidget(self.LabInterp)
        self.LabDate = QtWidgets.QLabel(self.layoutWidget)
        self.LabDate.setObjectName("LabDate")
        self.verticalLayout.addWidget(self.LabDate)
        self.LabAlmb = QtWidgets.QLabel(self.layoutWidget)
        self.LabAlmb.setObjectName("LabAlmb")
        self.verticalLayout.addWidget(self.LabAlmb)
        self.LabGen = QtWidgets.QLabel(self.layoutWidget)
        self.LabGen.setObjectName("LabGen")
        self.verticalLayout.addWidget(self.LabGen)
        self.ButonAct = QtWidgets.QPushButton(self.centralwidget)
        self.ButonAct.setGeometry(QtCore.QRect(440, 310, 141, 51))
        self.ButonAct.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButonAct.setObjectName("ButonAct")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 300, 131, 61))
        self.label.setObjectName("label")
        self.ArchivoR = QtWidgets.QLineEdit(self.centralwidget)
        self.ArchivoR.setGeometry(QtCore.QRect(160, 320, 241, 31))
        self.ArchivoR.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ArchivoR.setObjectName("ArchivoR")
        self.ArchivoR.returnPressed.connect(self.mostrar)
        DetallesEditar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(DetallesEditar)
        self.statusbar.setObjectName("statusbar")
        DetallesEditar.setStatusBar(self.statusbar)

        self.retranslateUi(DetallesEditar)
        QtCore.QMetaObject.connectSlotsByName(DetallesEditar)

        self.ButonAct.clicked.connect(self.actualizacion)
        
    eti1 = "Nombre"
    eti2 = "Interprete" 
    eti3 = "Album"      
    eti4 = "Fecha"   
    eti5 = "Genero"

    def retranslateUi(self, DetallesEditar):
        _translate = QtCore.QCoreApplication.translate
        DetallesEditar.setWindowTitle(_translate("DetallesEditar", "MainWindow"))
        self.LabAct.setText(_translate("DetallesEditar", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ACTUAL</span></p></body></html>"))
        self.LabNew.setText(_translate("DetallesEditar", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NUEVO(Edite)</span></p></body></html>"))
        self.LabName.setText(_translate("DetallesEditar", "NOMBRE:"))
        self.LabInterp.setText(_translate("DetallesEditar", "INTERPRETE:"))
        self.LabDate.setText(_translate("DetallesEditar", "FECHA:"))
        self.LabAlmb.setText(_translate("DetallesEditar", "ALBUM:"))
        self.LabGen.setText(_translate("DetallesEditar", "GENERO:"))
        self.ButonAct.setText(_translate("DetallesEditar", "ACTUALIZAR"))
        self.label.setText(_translate("DetallesEditar", "<html><head/><body><p>INTRODUZCA EL ARCHIVO A</p><p>EDITAR Y PRESS ENTER:</p></body></html>"))

    def mostrar(self):
        c = self.ArchivoR.text()
        n = buscador1.bus_nombre(c)
        try:
            self.actualname.setText(n[1])
            self.actualinterp.setText(n[2])
            self.actualalbm.setText(n[3])
            self.actualdate.setText(n[4])
            self.actualgen.setText(n[5])
        except:
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Aviso()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
                

    def actualizacion(self):
        c = self.ArchivoR.text()
        tx1 = self.newname.toPlainText()
        tx2 = self.newinterp.toPlainText()
        tx3 = self.newalbm.toPlainText()
        tx4 = self.newdate.toPlainText()
        tx5 = self.newgen.toPlainText()
        if tx1 == "" or tx2 == "" or tx3 == "" or tx4 == "" or tx5 == "":
            self.ventana = QtWidgets.QMainWindow()
            self.ui = Ui_Aviso()
            self.ui.setupUi(self.ventana)
            self.ventana.show()
        else:
            xml1.editar(c,self.eti1.lower(),tx1.capitalize())
            xml1.editar(c,self.eti2.lower(),tx2.capitalize())
            xml1.editar(c,self.eti3.lower(),tx3.capitalize())
            xml1.editar(c,self.eti4.lower(),tx4.capitalize())
            xml1.editar(c,self.eti5.lower(),tx5.capitalize())

###

class Ui_EditListas(object):
    def setupUi(self, EditListas):
        EditListas.setObjectName("EditListas")
        EditListas.resize(457, 440)
        EditListas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(EditListas)
        self.centralwidget.setObjectName("centralwidget")
        self.Elements = QtWidgets.QTextEdit(self.centralwidget)
        self.Elements.setGeometry(QtCore.QRect(20, 120, 241, 241))
        self.Elements.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Elements.setObjectName("Elements")
        self.Reached = QtWidgets.QTextEdit(self.centralwidget)
        self.Reached.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.Reached.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Reached.setObjectName("Reached")
        self.LabEl = QtWidgets.QLabel(self.centralwidget)
        self.LabEl.setGeometry(QtCore.QRect(20, 90, 241, 21))
        self.LabEl.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.LabEl.setObjectName("LabEl")
        self.ButonLis = QtWidgets.QPushButton(self.centralwidget)
        self.ButonLis.setGeometry(QtCore.QRect(0, 0, 0, 0))
        self.ButonLis.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButonLis.setObjectName("ButonLis")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 61))
        self.label.setObjectName("label")
        self.ListaName = QtWidgets.QLineEdit(self.centralwidget)
        self.ListaName.setGeometry(QtCore.QRect(150, 40, 261, 31))
        self.ListaName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ListaName.setObjectName("ListaName")
        self.Action = QtWidgets.QComboBox(self.centralwidget)
        self.Action.setGeometry(QtCore.QRect(290, 120, 151, 31))
        self.Action.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Action.setObjectName("Action")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 220, 131, 81))
        self.label_2.setObjectName("label_2")
        EditListas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EditListas)
        self.statusbar.setObjectName("statusbar")
        EditListas.setStatusBar(self.statusbar)

        self.retranslateUi(EditListas)
        QtCore.QMetaObject.connectSlotsByName(EditListas)

        self.ListaName.returnPressed.connect(self.LisShow)

    def retranslateUi(self, EditListas):
        _translate = QtCore.QCoreApplication.translate
        EditListas.setWindowTitle(_translate("EditListas", "MainWindow"))
        self.LabEl.setText(_translate("EditListas", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ELEMENTOS DE LA LISTA</span></p></body></html>"))
        self.ButonLis.setText(_translate("EditListas", "AGREGAR"))
        self.label.setText(_translate("EditListas", "<html><head/><body><p>INTRODUZCA LA </p><p>LISTA A VISUALIZAR:</p></body></html>"))
        self.Action.setItemText(0, _translate("EditListas", "VER ELEMENTOS"))
        self.Action.setItemText(1, _translate("EditListas", "AGREGAR ELEMENTO"))
        self.Action.setItemText(2, _translate("EditListas", "ELIMINAR ELEMENTO"))
        self.Action.setItemText(3, _translate("EditListas", "ELIMINAR LISTA"))
        self.label_2.setText("<html><head/><body><p align=\"center\">PRESIONE ENTER AL</p><p align=\"center\">INSERTAR EL NOMBRE DE</p><p align=\"center\">DE LA LISTA</p></body></html>")
        self.Action.activated.connect(self.boxaction)

    def LisShow(self):
        s = self.ListaName.text()
        if s in xml1.listas(1):
            self.Elements.setText(pintarNom(xml1.lis_list(1,s)))
        if s in xml1.listas(0):
            self.Elements.setText(pintarNom(xml1.lis_list(0,s)))
        if s in xml1.listas(2):
            self.Elements.setText(pintarNom(xml1.lis_list(2,s)))

    def boxaction(self):
        Item3 = self.Action.currentText()
        if Item3 == "VER ELEMENTOS":
            self.ListaName.returnPressed.connect(self.LisShow)
            self.LabEl.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ELEMENTOS DE LA LISTA</span></p></body></html>")
            self.label_2.setText("<html><head/><body><p align=\"center\">PRESIONE ENTER AL</p><p align=\"center\">INSERTAR EL NOMBRE DE</p><p align=\"center\">DE LA LISTA</p></body></html>")
            self.label_2.setGeometry(QtCore.QRect(300, 220, 131, 81))
            self.Reached.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.ButonLis.setGeometry(QtCore.QRect(0, 0, 0, 0))
            
        if Item3 == "AGREGAR ELEMENTO":
            self.label_2.setText("<html><head/><body><p align=\"center\">NOMBRE DEL ELEMENTO</p><p align=\"center\"> A AGREGAR:</p></body></html>")
            self.LabEl.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ELEMENTOS PARA AGREGAR</span></p></body></html>")
            self.Reached.setGeometry(QtCore.QRect(300, 280, 131, 51))
            self.label_2.setGeometry(QtCore.QRect(300, 220, 131, 51))
            self.ButonLis.setGeometry(QtCore.QRect(306, 350, 121, 41))
            self.ButonLis.setText("AGREGAR")
            self.ButonLis.clicked.connect(self.AgregarCan)

            s = self.ListaName.text()
            if s in xml1.listas(1):
                self.Elements.setText(pintarNom(defin.musica()))
            if s in xml1.listas(0):
                self.Elements.setText(pintarNom(defin.videos()))
            if s in xml1.listas(2):
                self.Elements.setText(pintarNom(defin.fotos()))
            

        if Item3 == "ELIMINAR ELEMENTO":
            self.label_2.setText("<html><head/><body><p align=\"center\">NOMBRE DEL ELEMENTO</p><p align=\"center\"> A ELIMINAR:</p></body></html>")
            self.LabEl.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ELEMENTOS PARA ELIMINAR</span></p></body></html>")
            self.Reached.setGeometry(QtCore.QRect(300, 280, 131, 51))
            self.label_2.setGeometry(QtCore.QRect(300, 220, 131, 51))
            self.ButonLis.setGeometry(QtCore.QRect(306, 350, 121, 41))
            self.ButonLis.setText("ELIMINAR")
            self.ButonLis.clicked.connect(self.EliminarCan)

            s = self.ListaName.text()
            if s in xml1.listas(1):
                self.Elements.setText(pintarNom(xml1.lis_list(1,s)))
            if s in xml1.listas(0):
                self.Elements.setText(pintarNom(xml1.lis_list(0,s)))
            if s in xml1.listas(2):
                self.Elements.setText(pintarNom(xml1.lis_list(2,s)))

        if Item3 == "ELIMINAR LISTA":
            self.label_2.setText("<html><head/><body><p align=\"center\">¿SEGURO DESEA</p><p align=\"center\">ELIMINAR LISTA?:</p></body></html>")
            self.LabEl.setText("<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">NO ME ELIMINES :'c</span></p></body></html>")
            self.Reached.setGeometry(QtCore.QRect(0, 0, 0, 0))
            self.ButonLis.setGeometry(QtCore.QRect(306, 350, 121, 41))
            self.ButonLis.setText("ELIMINAR LISTA")
            self.ButonLis.clicked.connect(self.EliminarLis)

    def AgregarCan(self):
        s = self.ListaName.text()
        bgg = self.Reached.toPlainText()
        
        if s in xml1.listas(1):
            self.Elements.setText(bgg+" agregado a "+s)
            xml1.cre_cancion(1, s, bgg)
        if s in xml1.listas(0):
            self.Elements.setText(bgg+" agregado a "+s)
            xml1.cre_cancion(0, s, bgg)
        if s in xml1.listas(2):
            self.Elements.setText(bgg+" agregado a "+s)
            xml1.cre_cancion(2, s, bgg)

    def EliminarCan(self):
        s = self.ListaName.text()
        bgg = self.Reached.toPlainText()
        
        if s in xml1.listas(1):
            self.Elements.setText(bgg+" eliminado de "+s)
            xml1.eli_cancion(1, s, bgg)
        if s in xml1.listas(0):
            self.Elements.setText(bgg+" eliminado de "+s)
            xml1.eli_cancion(0, s, bgg)
        if s in xml1.listas(2):
            self.Elements.setText(bgg+" eliminado de "+s)
            xml1.eli_cancion(2, s, bgg)

    def EliminarLis(self):
        s = self.ListaName.text()

        if s in xml1.listas(1):
            self.Elements.setText(s+" a sido eliminada")
            xml1.eli_list(1,s)
        if s in xml1.listas(0):
            self.Elements.setText(s+" a sido eliminada")
            xml1.eli_list(0,s)
        if s in xml1.listas(2):
            self.Elements.setText(s+" a sido eliminada")
            xml1.eli_list(2,s)
            
        

###

class Ui_CreaListas(object):
    def setupUi(self, CreaListas):
        CreaListas.setObjectName("CreaListas")
        CreaListas.resize(457, 422)
        CreaListas.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(CreaListas)
        self.centralwidget.setObjectName("centralwidget")
        self.Elements = QtWidgets.QTextEdit(self.centralwidget)
        self.Elements.setGeometry(QtCore.QRect(20, 120, 241, 241))
        self.Elements.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Elements.setObjectName("Elements")
        self.Reached = QtWidgets.QTextEdit(self.centralwidget)
        self.Reached.setGeometry(QtCore.QRect(300, 280, 131, 51))
        self.Reached.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Reached.setObjectName("Reached")
        self.LabEl = QtWidgets.QLabel(self.centralwidget)
        self.LabEl.setGeometry(QtCore.QRect(20, 90, 241, 21))
        self.LabEl.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.LabEl.setObjectName("LabEl")
        self.ButonLis = QtWidgets.QPushButton(self.centralwidget)
        self.ButonLis.setGeometry(QtCore.QRect(306, 350, 121, 41))
        self.ButonLis.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButonLis.setObjectName("ButonLis")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 61))
        self.label.setObjectName("label")
        self.ListaName = QtWidgets.QTextEdit(self.centralwidget)
        self.ListaName.setGeometry(QtCore.QRect(140, 40, 271, 31))
        self.ListaName.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ListaName.setObjectName("ListaName")
        self.Action = QtWidgets.QComboBox(self.centralwidget)
        self.Action.setGeometry(QtCore.QRect(290, 150, 151, 31))
        self.Action.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Action.setObjectName("Action")
        self.Action.addItem("")
        self.Action.addItem("")
        self.Action.addItem("")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(300, 220, 131, 51))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(290, 120, 141, 16))
        self.label_3.setObjectName("label_3")
        CreaListas.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CreaListas)
        self.statusbar.setObjectName("statusbar")
        CreaListas.setStatusBar(self.statusbar)

        self.retranslateUi(CreaListas)
        QtCore.QMetaObject.connectSlotsByName(CreaListas)

    def retranslateUi(self, CreaListas):
        _translate = QtCore.QCoreApplication.translate
        CreaListas.setWindowTitle(_translate("CreaListas", "MainWindow"))
        self.LabEl.setText(_translate("CreaListas", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">ARCHIVOS A AGREGAR</span></p></body></html>"))
        self.ButonLis.setText(_translate("CreaListas", "AGREGAR"))
        self.label.setText(_translate("CreaListas", "<html><head/><body><p>NOMBRE DE LA</p><p>NUEVA LISTA :</p></body></html>"))
        self.Action.setItemText(0, _translate("CreaListas", "MUSICA"))
        self.Action.setItemText(1, _translate("CreaListas", "VIDEOS"))
        self.Action.setItemText(2, _translate("CreaListas", "IMAGENES"))
        self.label_2.setText(_translate("CreaListas", "<html><head/><body><p align=\"center\">NOMBRE DEL ELEMENTO</p><p align=\"center\"> A AGREGAR:</p></body></html>"))
        self.label_3.setText(_translate("CreaListas", "TIPO DE LISTA:"))

        self.Action.activated.connect(self.Type)

    def Type(self):
        Item1 = self.Action.currentText()
        if Item1 == "MUSICA":
            self.Elements.setText(pintarNom(defin.musica()))
            self.ButonLis.clicked.connect(self.CLM)
                                  
        elif Item1 == "VIDEOS":
            self.Elements.setText(pintarNom(defin.videos()))
            self.ButonLis.clicked.connect(self.CLV)
                                  
        elif Item1 == "IMAGENES":
            self.Elements.setText(pintarNom(defin.fotos()))
            self.ButonLis.clicked.connect(self.CLI)

    def CLM(self):
        nom = self.ListaName.toPlainText()
        bgg = self.Reached.toPlainText()
        if nom == "" or bgg == "":
            return
        else:
            xml1.cre_list(1,nom)
            xml1.cre_cancion(1,nom,bgg)

    def CLV(self):
        nom = self.ListaName.toPlainText()
        bgg = self.Reached.toPlainText()
        if nom == "" or bgg == "":
            return
        else:
            xml1.cre_list(0,nom)
            xml1.cre_cancion(0,nom,bgg)

    def CLI(self):
        nom = self.ListaName.toPlainText()
        bgg = self.Reached.toPlainText()
        if nom == "" or bgg == "":
            return
        else:
            xml1.cre_list(2,nom)
            xml1.cre_cancion(2,nom,bgg)
        
        
###

class Ui_VentAgregar(QMainWindow):
    def setupUi(self, VentAgregar):
        VentAgregar.setObjectName("VentAgregar")
        VentAgregar.resize(441, 440)
        VentAgregar.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(170, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(VentAgregar)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(22, 120, 20, 231))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.NuevNom = QtWidgets.QTextEdit(self.centralwidget)
        self.NuevNom.setGeometry(QtCore.QRect(160, 120, 241, 31))
        self.NuevNom.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NuevNom.setObjectName("NuevNom")
        self.NuevoFech = QtWidgets.QTextEdit(self.centralwidget)
        self.NuevoFech.setGeometry(QtCore.QRect(160, 220, 241, 31))
        self.NuevoFech.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NuevoFech.setObjectName("NuevoFech")
        self.NuevGen = QtWidgets.QTextEdit(self.centralwidget)
        self.NuevGen.setGeometry(QtCore.QRect(160, 320, 241, 31))
        self.NuevGen.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NuevGen.setObjectName("NuevGen")
        self.NuevAlbm = QtWidgets.QTextEdit(self.centralwidget)
        self.NuevAlbm.setGeometry(QtCore.QRect(160, 270, 241, 31))
        self.NuevAlbm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NuevAlbm.setObjectName("NuevAlbm")
        self.LabNew = QtWidgets.QLabel(self.centralwidget)
        self.LabNew.setGeometry(QtCore.QRect(232, 90, 101, 21))
        self.LabNew.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.LabNew.setObjectName("LabNew")
        self.Nuevinterp = QtWidgets.QTextEdit(self.centralwidget)
        self.Nuevinterp.setGeometry(QtCore.QRect(160, 170, 241, 31))
        self.Nuevinterp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Nuevinterp.setObjectName("Nuevinterp")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(42, 120, 71, 231))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.LabName = QtWidgets.QLabel(self.layoutWidget)
        self.LabName.setObjectName("LabName")
        self.verticalLayout.addWidget(self.LabName)
        self.LabInterp = QtWidgets.QLabel(self.layoutWidget)
        self.LabInterp.setObjectName("LabInterp")
        self.verticalLayout.addWidget(self.LabInterp)
        self.LabDate = QtWidgets.QLabel(self.layoutWidget)
        self.LabDate.setObjectName("LabDate")
        self.verticalLayout.addWidget(self.LabDate)
        self.LabAlmb = QtWidgets.QLabel(self.layoutWidget)
        self.LabAlmb.setObjectName("LabAlmb")
        self.verticalLayout.addWidget(self.LabAlmb)
        self.LabGen = QtWidgets.QLabel(self.layoutWidget)
        self.LabGen.setObjectName("LabGen")
        self.verticalLayout.addWidget(self.LabGen)
        self.ButonAgr = QtWidgets.QPushButton(self.centralwidget)
        self.ButonAgr.setGeometry(QtCore.QRect(130, 380, 121, 41))
        self.ButonAgr.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.ButonAgr.setObjectName("ButonAgr")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 61))
        self.label.setObjectName("label")
        self.NuevArch = QtWidgets.QTextEdit(self.centralwidget)
        self.NuevArch.setGeometry(QtCore.QRect(140, 40, 271, 31))
        self.NuevArch.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NuevArch.setObjectName("NuevArch")
        VentAgregar.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VentAgregar)
        self.statusbar.setObjectName("statusbar")
        VentAgregar.setStatusBar(self.statusbar)

        self.retranslateUi(VentAgregar)
        QtCore.QMetaObject.connectSlotsByName(VentAgregar)

        self.ButonAgr.clicked.connect(self.guardar)

    def retranslateUi(self, VentAgregar):
        _translate = QtCore.QCoreApplication.translate
        VentAgregar.setWindowTitle(_translate("VentAgregar", "MainWindow"))
        self.LabNew.setText(_translate("VentAgregar", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">DATOS</span></p></body></html>"))
        self.LabName.setText(_translate("VentAgregar", "NOMBRE:"))
        self.LabInterp.setText(_translate("VentAgregar", "INTERPRETE:"))
        self.LabDate.setText(_translate("VentAgregar", "FECHA:"))
        self.LabAlmb.setText(_translate("VentAgregar", "ALBUM:"))
        self.LabGen.setText(_translate("VentAgregar", "GENERO:"))
        self.ButonAgr.setText(_translate("VentAgregar", "AGREGAR"))
        self.label.setText(_translate("VentAgregar", "<html><head/><body><p>INTRODUZCA EL </p><p>NUEVO ARCHIVO:</p></body></html>"))

    def guardar(self):
        arc = self.NuevArch.toPlainText()
        NI = self.Nuevinterp.toPlainText()
        NA = self.NuevAlbm.toPlainText()
        ND = self.NuevoFech.toPlainText()
        NG = self.NuevGen.toPlainText()
        archivo1.agregar(arc)
        xml1.actualizar(NI,NA,ND,NG)
        
        
###

     
def pintarNom(l):
    jj = ""
    for i in range(len(l)):
        jj += (l[i])
        jj += '\n'
        jj += " "
        jj += '\n'
    return jj

def pintarDet(n):
    nn = ""
    for i in range(len(n)):
        nn += (n[i])
        nn += '\n'
    return nn


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
