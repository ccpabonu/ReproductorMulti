# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reproductor.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(821, 601)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"background-color: rgb(85, 170, 255);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lista = QtWidgets.QTreeWidget(self.centralwidget)
        self.lista.setObjectName("lista")
        self.gridLayout.addWidget(self.lista, 6, 2, 1, 1)
        self.musica = QtWidgets.QPushButton(self.centralwidget)
        self.musica.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.musica.setObjectName("musica")
        self.gridLayout.addWidget(self.musica, 14, 2, 1, 1)
        self.video = QtWidgets.QPushButton(self.centralwidget)
        self.video.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.video.setObjectName("video")
        self.gridLayout.addWidget(self.video, 15, 2, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 13, 2, 1, 1)
        self.editar = QtWidgets.QPushButton(self.centralwidget)
        self.editar.setStyleSheet("background-color: rgb(255, 255, 127);")
        self.editar.setObjectName("editar")
        self.gridLayout.addWidget(self.editar, 3, 0, 1, 1)
        self.imagen = QtWidgets.QPushButton(self.centralwidget)
        self.imagen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"")
        self.imagen.setObjectName("imagen")
        self.gridLayout.addWidget(self.imagen, 16, 2, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("font: 75 8pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setStyleSheet("color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);")
        self.comboBox.setEditable(True)
        self.comboBox.setMaxVisibleItems(2)
        self.comboBox.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox.setDuplicatesEnabled(False)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 2, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(100, 10, 112, 24))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(250, 10, 112, 24))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_3.setGeometry(QtCore.QRect(400, 10, 112, 24))
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox)
        self.radioButton_4.setGeometry(QtCore.QRect(540, 10, 112, 24))
        self.radioButton_4.setObjectName("radioButton_4")
        self.gridLayout.addWidget(self.groupBox, 0, 2, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 25))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lista.headerItem().setText(0, _translate("MainWindow", "Nombre"))
        self.lista.headerItem().setText(1, _translate("MainWindow", "Autor"))
        self.lista.headerItem().setText(2, _translate("MainWindow", "Genero"))
        self.lista.headerItem().setText(3, _translate("MainWindow", "Fecha"))
        self.lista.headerItem().setText(4, _translate("MainWindow", "Tipo"))
        self.musica.setText(_translate("MainWindow", "MUSICA"))
        self.video.setText(_translate("MainWindow", "VIDEOS"))
        self.pushButton.setText(_translate("MainWindow", "TODO"))
        self.editar.setText(_translate("MainWindow", "EDITAR ARCHIVOS"))
        self.imagen.setText(_translate("MainWindow", "IMAGENES"))
        self.label_4.setToolTip(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">INTRODUZCA EL NOMBRE DEL</span></p><p align=\"center\"><span style=\" font-weight:600;\">ARCHIVO QUE DESEA AGREGAR</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p align=\"justify\">ESCOGA UNA ACCION:</p></body></html>"))
        self.comboBox.setProperty("currentText", _translate("MainWindow", "EDITAR"))
        self.comboBox.setItemText(0, _translate("MainWindow", "EDITAR"))
        self.comboBox.setItemText(1, _translate("MainWindow", "AGREGAR"))
        self.comboBox.setItemText(2, _translate("MainWindow", "ALBUMES"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">¡BIENVENIDO!</span></p></body></html>"))
        self.groupBox.setTitle(_translate("MainWindow", "Filtrar:"))
        self.radioButton.setText(_translate("MainWindow", "Todo"))
        self.radioButton_2.setText(_translate("MainWindow", "Musica"))
        self.radioButton_3.setText(_translate("MainWindow", "Imagenes"))
        self.radioButton_4.setText(_translate("MainWindow", "Video"))

    def listar(self):
        """Esta funciòn llena la lista de archivos"""
        self.lista.clear() # Limpia la lista
        #llenar la lista
        archivo = []
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
