# -*- coding: utf-8 -*-
"""
Reproductor de archivos media primera entrega
"""
# Llamado a librerias

# se importa la libreria de interfaz grafica
import xml.etree.ElementTree as et
# se importa una libreria para manejo especifico de archivos xml
import os
# libreria para la interacción de python con el sistema operativo
from bs4 import BeautifulSoup
# Libreria para dar formato al texto xml

import shutil

# Definición de variables globales
# directorio = os.path.join(os.path.realpath(__file__))
archivo = os.path.join('metadata1.xml')  # contiene la ruta del archivo xml
tree = et.parse(archivo)  # carga el contenido del archivo xml a memoria
raiz = tree.getroot()  # define la estructura jerarquica del archivo
files = os.listdir()  # lista de archivos que contiene la carpeta donde esta el programa
objetos = raiz.findall('.//archivo')  # carga de todos los archivos que estan en conocimiento como objetos etree
l_objetos = []  # lista los nombres de los archivos que estan en conocimiento

datos = ['metadata.xml', 'gui.py', 'main.py', 'nuevo1.xml', 'lol.py']  # objetos de los archivos propios del programa
# se definen las extensiones de los archivos para clasificarlos luego
vidext = ['mp4', 'mov', 'avi', 'm4v', 'mpg', 'swf']
fotext = ['jpg', 'png', 'bmp', 'pdf']
musext = ['mp3', 'wma', 'wav', 'ac3', 'cda']


class Texto():
    """Es la super clase que contiene funciones comunes a las demas"""
    def depurar(self, text):
        """Esta funcion se usa para normalizar texto y se define aca porque se utiliza para el contenido de las variables,
        existen dos funciones depurar porque una reemplaza el punto y la otra no"""
        return text.replace(',', '_').replace('\'', '').replace(' ', '').replace('.', '').replace('"', '').replace('[', '').replace(']', '').replace('\n', '')

    def depurar1(self, text):
        """Esta funcion se usa para normalizar texto y se define aca porque se utiliza para el contenido de las variables"""
        return text.replace(',', '_').replace('\'', '').replace(' ', '').replace('"', '').replace('[', '').replace(']', '').replace('\n', '')


    def escribir(self):
        """Escribe los cambios en el archivo xml"""
        tree.write('metadata1.xml')
        bs = BeautifulSoup(open('metadata1.xml'), 'xml')
        archivo1 = open('metadata1.xml', "w+")
        archivo1.write(bs.prettify())


class Archivos(Texto):
    """Clase que interactua con los archivos media"""
    def __init__(self):
        objetos = raiz.findall('.//archivo')  # carga de todos los archivos que estan en conocimiento como objetos etree
        l_objetos = []  # lista los nombres de los archivos que estan en conocimiento
        for i in objetos:
            l_objetos.append(self.depurar1(i.text))

    def listar(self):
        """lista los archivos a cargar"""
        self.lis = []
        for a in os.listdir('.'):
            if self.depurar1(a) not in l_objetos and self.depurar1(a) not in datos and(a.split('.')[-1] in vidext or a.split('.')[-1] in fotext or a.split('.')[-1] in musext):
                self.lis.append(a)
        return self.lis

    def agregar(self, arch0):
        self.arch0 = arch0
        self.arch = self.arch0
        if self.arch not in os.listdir('./data/'):
            shutil.move(self.arch, './data/')

    def eliminar(self, arch0):
        self.arch0 = arch0
        self.arch = self.arch0
        if self.arch in os.listdir('./data/'):
            shutil.move('./data/'+self.arch, '.')
        for i in [0, 1, 2]:
            for e in raiz[i].findall('archivo'):
                if e.text:
                    if self.arch == self.depurar1(e.text):
                        raiz[i].remove(e)
        self.escribir()



class Definir(Texto):
    """Clase que caracteriza los archivos dependiendo de la extencion"""

    # Definición de funciones
    def categorias(self):
        """Devuelve las posibles categorias de los archivos (video, musica y fotos)"""
        self.__cat = []
        for etq in raiz:
            self.__cat.append(etq.tag)
        return self.__cat.sort()

    def videos(self):
        """Devuelve una lista los archivos que son video de la base de datos y los ordena alfebeticamente"""
        self.__vi = []
        for etq in raiz[0]:
            # print(depurar1(etq.text))
            self.__vi.append(self.depurar1(etq.text))
        self.__vi.sort()
        return self.__vi

    def musica(self):
        """Devuelve una lista los archivos que son musica de la base de datos y los ordena alfebeticamente"""
        self.__mus = []
        for etq in raiz[1]:
            self.__mus.append(self.depurar1(etq.text))
        self.__mus.sort()
        return self.__mus

    def fotos(self):
        """Devuelve una lista los archivos que son fotos de la base de datos y los ordena alfebeticamente"""
        self.__fot = []
        for etq in raiz[2]:
            self.__fot.append(self.depurar1(etq.text))
        self.__fot.sort()
        return self.__fot

    def todos(self):
        "Devuelve una lista de todos los archivos"
        self. __tod = []
        for etq in raiz[0]:
            self.__tod.append(self.depurar1(etq.text))
        for etq in raiz[1]:
            self.__tod.append(self.depurar1(etq.text))
        for etq in raiz[2]:
            self.__tod.append(self.depurar1(etq.text))
        return self.__tod


class XML(Texto):
    """Clase que edita el archivo xml segun la necesidad"""

    def actualizar(self):
        objetos = raiz.findall('.//archivo')  # carga de todos los archivos que estan en conocimiento como objetos etree
        l_objetos = []  # lista los nombres de los archivos que estan en conocimiento
        for i in objetos:
            l_objetos.append(self.depurar1(i.text))
        """Busca archivos nuevos en la carpeta y revisa si existen en la base datos sino existen los crea."""
        files = os.listdir('./data/')
        for f in files:
            if self.depurar1(f) not in l_objetos and self.depurar1(f) not in datos:
                # print(f + '  !!!!! ' + ' no esta en la lista')
                # print(f.split('.')[-1])
                if f.split('.')[-1] not in vidext and f.split('.')[-1] not in fotext and f.split('.')[-1] not in musext:
                    pass
                    # print(f)
                    # print('El programa no soporta este tipo de archivo')
                else:
                    # print('se actualiza ' + f)
                    if f.split('.')[-1] in vidext:
                        # print('es video')
                        et.SubElement(raiz[0], 'archivo')
                        raiz[0][-1].text = f
                        # print(raiz[0][-1].text)
                        et.SubElement(raiz[0][-1], 'nombre')
                        raiz[0][-1].find('nombre').text = self.depurar(str(f.split('.')[:-1]))
                        et.SubElement(raiz[0][-1], 'interprete')
                        et.SubElement(raiz[0][-1], 'album')
                        et.SubElement(raiz[0][-1], 'fecha')
                        et.SubElement(raiz[0][-1], 'genero')
                        raiz[0][-1].find('interprete').text = "Desconocido"
                        raiz[0][-1].find('album').text = "Desconocido"
                        raiz[0][-1].find('fecha').text = "Desconocido"
                        raiz[0][-1].find('genero').text = "Desconocido"

                        # for x in raiz[0][-1]:
                        #     print(x.tag + ' : ' +x.text)
                    if f.split('.')[-1] in musext:
                        # print('es musica')
                        et.SubElement(raiz[1], 'archivo')
                        raiz[1][-1].text = f
                        # print(raiz[1][-1].text)
                        et.SubElement(raiz[1][-1], 'nombre')
                        raiz[1][-1].find('nombre').text = self.depurar(str(f.split('.')[:-1]))
                        et.SubElement(raiz[1][-1], 'interprete')
                        et.SubElement(raiz[1][-1], 'album')
                        et.SubElement(raiz[1][-1], 'fecha')
                        et.SubElement(raiz[1][-1], 'genero')
                        raiz[1][-1].find('interprete').text = "Desconocido"
                        raiz[1][-1].find('album').text = "Desconocido"
                        raiz[1][-1].find('fecha').text = "Desconocido"
                        raiz[1][-1].find('genero').text = "Desconocido"
                    if f.split('.')[-1] in fotext:
                        #print('es foto')
                        et.SubElement(raiz[2], 'archivo')
                        raiz[2][-1].text = f
                        # print(raiz[2][-1].text)
                        et.SubElement(raiz[2][-1], 'nombre')
                        raiz[2][-1].find('nombre').text = self.depurar(str(f.split('.')[:-1]))
                        et.SubElement(raiz[2][-1], 'interprete')
                        et.SubElement(raiz[2][-1], 'album')
                        et.SubElement(raiz[2][-1], 'fecha')
                        et.SubElement(raiz[2][-1], 'genero')
                        raiz[2][-1].find('interprete').text = "Desconocido"
                        raiz[2][-1].find('album').text = "Desconocido"
                        raiz[2][-1].find('fecha').text = "Desconocido"
                        raiz[2][-1].find('genero').text = "Desconocido"
        self.escribir()

    def editar(self, titulo, eti, texto):
        self.titulo = titulo
        self.eti = eti
        self.etiq = './/' + self.eti
        """edita el campo que se quiera en el archivo"""
        for x in raiz.findall('.//archivo'):
            if self.titulo in x.text:
                # print(x.find(eti).tag)
                # print(depurar(x.find(eti).text))
                x.find(self.etiq).text = texto
                break
        self.escribir()

    def cre_list(self, nom):
        self.nom = nom
        self.pos = 1
        """Esta funcion crea una lista para videos = 0, musica = 1 o fotos = 2 segun sea el caso"""
        et.SubElement(raiz[3][self.pos], 'lista')
        (raiz[3][self.pos][-1]).text = self.nom
        self.escribir()

    def eli_list(self, nom):
        self.nom = nom
        self.pos = 1
        """se elimina una lista especifica segun videos = 0, musica = 1 o fotos = 2 segun sea el caso
        nom = nombre de lista"""
        for e in raiz[3][self.pos].findall('lista'):
            if e.text:
                if self.nom == self.depurar1(e.text):
                    raiz[3][self.pos].remove(e)
        self.escribir()

    def cre_cancion(self, nom, can):
        self.nom = nom
        self.pos = 1
        self.can = can
        """Esta funcion crea canciones en las listas segun videos = 0, musica = 1 o fotos = 2 segun sea el caso
        nom = nombre de lista, can = nombre de la cancion"""
        for e in raiz[3][self.pos].findall('lista'):
            if e.text:
                if self.nom == self.depurar1(e.text):
                    et.SubElement(e, 'cancion')
                    e[-1].text = self.can
        self.escribir()

    def eli_cancion(self, nom, can):
        self.nom = nom
        self.pos = 1
        self.can = can
        """se elimina una cancion de una lista especifica segun videos = 0, musica = 1 o fotos = 2 segun sea el caso
        nom = nombre de lista"""
        for e in raiz[3][self.pos].findall('lista'):
            if e.text:
                if self.nom == self.depurar1(e.text):
                    for j in e:
                        if self.depurar1(j.text) == self.can:
                            e.remove(j)
        self.escribir()

    def lis_list(self, nom):
        self.nom = nom
        self.pos = 1
        """lista el contenido de una lista especifica segun videos = 0, musica = 1 o fotos = 2 segun sea el caso
        nom = nombre de lista"""
        self.can = []
        for e in raiz[3][self.pos].findall('lista'):
            if e.text:
                if self.nom == self.depurar1(e.text):
                    for j in e:
                        self.can.append(self.depurar1(j.text))
        return self.can

    def listas(self, pos = 1):
        self.pos = pos
        """lista las listas especifica segun videos = 0, musica = 1 o fotos = 2 segun sea el caso
        nom = nombre de lista"""
        self.can = []
        for e in raiz[3][self.pos].findall('lista'):
            self.can.append(self.depurar1(e.text))
        return self.can


class Buscadores(Texto):
    """Clase que busca y entrega informacion almacenada en el archivo xml"""

    def bus_nombre(self, texto):
        """Salida: archivo,nombre, interprete, album, fecha, genero """
        self.nom = []
        for x in raiz.findall('.//archivo'):
            if texto in x.text:
                self.nom.append(self.depurar1(x.text))
                for et in x:
                    self.nom.append(self.depurar1(et.text))
                break
        return self.nom

    def tag_vid(self, eti):
        self.eti = eti
        """Lista todos los valores de un tag especifico de videos (ej: todos los generos que existen) """
        self.vid = []
        self.etiq = './/' + self.eti
        for x in raiz[0].findall(self.etiq):
            # print(x.text)
            self.vid.append(self.depurar1(x.text))
        self.vid = list(set(self.vid))
        self.vid.sort()
        return self.vid

    def tag_mus(self, eti):
        self.eti = eti
        """Lista todos los valores de un tag especifico de musica (ej: todos los generos que existen) """
        self.vid = []
        self.etiq = './/' + self.eti
        for x in raiz[1].findall(self.etiq):
            # print(x.text)
            self.vid.append(self.depurar1(x.text))
        self.vid = list(set(self.vid))
        self.vid.sort()
        return self.vid

    def tag_fot(self, eti):
        self.eti = eti
        """Lista todos los valores de un tag especifico de fotos (ej: todos los generos que existen) """
        self.vid = []
        self.etiq = './/' + self.eti
        for x in raiz[0].findall(self.etiq):
            # print(x.text)
            self.vid.append(self.depurar1(x.text))
        self.vid = list(set(self.vid))
        self.vid.sort()
        return self.vid

    def bus_tag_vid(self, eti, valor):
        self.eti = eti
        self.valor = valor
        """Lista todos los valores de un video con un tag especifico y su valor (ej: todos los videos de genero tube)"""
        self.vid = []
        self.etiq = './/'+ self.eti
        # #print(raiz[0].findall(etiq))
        for x in raiz[0]:
            if self.valor in x.find(self.etiq).text:
                self.vid.append(self.depurar1(x.text))
                #print(x.find(etiq).text)
                for y in x:
                 #   print(depurar(y.text))
                    self.vid.append(self.depurar(y.text))
        return self.vid

    def bus_tag_mus(self, eti, valor):
        self.eti = eti
        self.valor = valor
        """Lista todos los valores de un audio con un tag especifico y su valor (ej: todos los videos de genero tube)"""
        self.vid = []
        self.etiq = './/'+ self.eti
        # #print(raiz[0].findall(etiq))
        for x in raiz[1]:
            if self.valor in x.find(self.etiq).text:
                self.vid.append(self.depurar1(x.text))
                #print(x.find(etiq).text)
                for y in x:
                 #   print(depurar(y.text))
                    self.vid.append(self.depurar(y.text))
        return self.vid

    def bus_tag_fot(self, eti, valor):
        self.eti = eti
        self.valor = valor
        """Lista todos los valores de una imagen con un tag especifico y su valor (ej: todos los videos de genero tube)"""
        self.vid = []
        self.etiq = './/'+ self.eti
        # #print(raiz[0].findall(etiq))
        for x in raiz[2]:
            if self.valor in x.find(self.etiq).text:
                self.vid.append(self.depurar1(x.text))
                #print(x.find(etiq).text)
                for y in x:
                 #   print(depurar(y.text))
                    self.vid.append(self.depurar(y.text))
        return self.vid

arch = Archivos()
salida = XML()
#print(arch.listar())
#arch.agregar('../video3.mp4')
#salida.actualizar()
#lista = Definir()
#print(lista.todos())
#salida.editar("xxxx1.mp4", "album", "Hola2")