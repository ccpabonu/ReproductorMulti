
import data.main as main                                                         #Importa todas las funciones y clases creadas en el archivo main.py
import os

"--------------------------------------------------------------------------------------------------------------------------------------------------------------------"
#Creamos objetos de cada clase que usaremos en la interfaz
buscador1 = main.Buscadores()
definir1 = main.Definir()
archivo1 = main.Archivos()
xml1 = main.XML()


def mainW ():



    "pantalla principal del programa"
    print("----------------------------REPRODUCTOR MULTIMEDIA-----------------------------")
    print("1. MUSICA")
    print("2. VIDEOS")
    print("3. IMAGENES")
    print("4. AGREGAR CONTENIDO")
    print("5. SALIR")
    a=input("Escoja la Opción : \n")

    if a=="1":
        os.system("cls")

        t="MUSICA"
        multimediaW(t)
    elif a=="2":
        os.system('cls')
        t ="VIDEOS"
        multimediaW(t)
    elif a=="3":
        os.system('cls')
        t = "IMAGENES"
        multimediaW(t)
    elif a=="4":
        os.system('cls')
        if not archivo1.listar():
            print('No hay posibles archivos para agregar.')
        else:
            print("Posibles archivos para agregar:")
            for i in archivo1.listar():
                print(i)
            arch = str(input('Escoja el archivo: \n'))
            archivo1.agregar(arch)
            xml1.actualizar()
        mainW()
    elif a=="5":
        print("BYE")
    else:
        os.system('cls')

        print("Introduzca un valor correcto")
        mainW()
def multimediaW(t):

    "Funcion multimedia que recibe 't' como parametro para reconocer si es el menu mltimedia de Musica,Videos o Imagenes"
    print()
    print("----------------------------"+t+"-----------------------------")
    print("1. Ver "+t.capitalize())
    print("2. Ver Albumes")
    print("3. Ver Listas de reproducción")
    print("4. Atras")
    print()
    a = input("Escoja una Opción : \n")
    print()
    os.system('cls')
    if a=="1":

        if t=="MUSICA":
            pintarNom(definir1.musica())                                                  #Pinta el arreglo devuelto por musica() que son el nombre de todos los archivos musica
            print()                                                                   #existentes en multimedia
            print("1. Detalles o Editar")
            print("2. Busqueda")
            print("3. Atras")
            b = int(input("Escoja un opción : \n"))
            if b==1:
                c=input("Escriba el nombre del archivo : \n")
                n=buscador1.bus_nombre(c)                                                  #Busca los detalles del archivo con el nombre del archivo y los pinta
                pintarDet(n)
                d=input("¿Desea editar? S / N  \n")
                if d.upper()=="S":
                    eti=str(input("¿Que atributo desea editar?"))
                    txt=str(input("Escriba el cambio  "))
                    xml1.editar(c,eti.lower(),txt.capitalize())                         #Llama la funcion editar que recibe 3 parametros, el nombre de archivo, atributo a modificar
                    multimediaW(t)
                   #print("edito")                                                      #y el nuevo valor
                else :
                    multimediaW(t)

            elif b==2:
                os.system('cls')
                pintarBusM(t)
            else:
                multimediaW(t)
        elif t=="VIDEOS":
            pintarNom(definir1.videos())
            print()
            print("1. Detalles o Editar")
            print("2. Busqueda")
            print("3. Atras")
            b = int(input("Escoja un opción : \n"))
            if b == 1:
                c = input("Escriba el nombre del archivo : \n")
                n = buscador1.bus_nombre(c)
                pintarDet(n)
                d = input("¿Desea editar? S / N  \n")
                if d.upper() == "S":
                    eti = str(input("¿Que atributo desea editar?"))
                    txt = str(input("Escriba el cambio  "))
                    xml1.editar(c, eti.lower(), txt.capitalize())
                    multimediaW(t)
                # print("edito")
                else:
                    multimediaW(t)

            elif b == 2:
                os.system('cls')
                pintarBusV(t)
            else:
                multimediaW(t)
        else :
            pintarNom(definir1.fotos())
            print()
            print("1. Detalles o Editar")
            print("2. Busqueda")
            print("3. Atras")
            b = int(input("Escoja un opción : \n"))
            if b == 1:
                c = input("Escriba el nombre del archivo : \n")
                n = buscador1.bus_nombre(c)
                pintarDet(n)
                d = input("¿Desea editar? S / N  \n")
                if d.upper() == "S":
                    eti = str(input("¿Que atributo desea editar?"))
                    txt = str(input("Escriba el cambio  "))
                    xml1.editar(c, eti.lower(), txt.capitalize())
                    multimediaW(t)
                # print("edito")
                else:
                    multimediaW(t)

            elif b == 2:
                os.system('cls')
                pintarBusI(t)
            else:
                multimediaW(t)
    elif a=="2":
        os.system('cls')
        if t=="MUSICA":
            print("-------------ALBUMES------------")
            pintarAlbM(t)
        elif t=="VIDEOS":
            print("-------------ALBUMES------------")
            pintarAlbV(t)
        else:
            print("-------------ALBUMES------------")
            pintarAlbI(t)
    elif a=="3":
        if t=="MUSICA":
            pintarListM(t)
        elif t=="VIDEOS":
            pintarListV(t)
        elif t=="IMAGENES":
            pintarListI(t)
        else:
            multimediaW(t)

    elif a=="4":
        mainW()
    else:
        print("Introduzca un valor correcto")
        multimediaW(t)
def pintarNom(l):
    "funcion que pinta un arreglo "
    for i in range(len(l)):
        print(l[i])

def pintarDet(n):
    "funcion que recibe un arreglo con la info del archivo y pinta de una mejor manera "
    print("Nombre Archivo : " + n[0] + "    Nombre : " + n[1] + "    Interpetre : " + n[2])
    print("Album : " + n[3] + "    Fecha : " + n[4] + "    Genero: " + n[5])
def pintarBusM(t):
    "funcion que crea y pinta el menu de busqueda para la musica"
    print("Buscar por : ")
    print("1. Nombre")
    print("2. Autor")
    print("3. Fecha")
    print("4. Genero")
    bb = int(input("Escoja un opción : \n"))
    if bb==1:
        c = input("Escriba el nombre: \n")
        print("Cancion con este nombre :")
        pintarNom(buscador1.bus_tag_mus('nombre',c) )
        c = input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)

    elif bb==2:
        c = input("Escriba el autor: \n")
        print("Canciones con ese interpetre :")
        pintarNom(buscador1.bus_tag_mus('interpetre', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
    elif bb==3:
        c = input("Escriba el Fecha: \n")
        print("Canciones de ese Fecha :")
        pintarNom(buscador1.bus_tag_mus('fecha', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
    elif bb==4:
        c = input("Escriba el Genero \n")
        print("Canciones de ese genero :")
        pintarNom(buscador1.bus_tag_mus('genero', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
def pintarBusV(t):
    "funcion que crea y pinta el menu de busqueda para los videos"
    print("Buscar por : ")
    print("1. Nombre")
    print("2. Interpetre")
    print("3. Fecha")
    print("4. Genero")
    bb = int(input("Escoja un opción : \n"))
    if bb==1:
        c = input("Escriba el nombre: \n")
        print("Video con este nombre :")
        pintarNom(buscador1.bus_tag_vid('nombre',c) )
        c = input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)

    elif bb==2:
        c = input("Escriba el interprete: \n")
        print("Videos de ese interprete :")
        pintarNom(buscador1.bus_tag_vid('interprete', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
    elif bb==3:
        c = input("Escriba el Fecha: \n")
        print("Videos de ese Fecha :")
        pintarNom(buscador1.bus_tag_vid('fecha', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
    elif bb==4:
        c = input("Escriba el Genero \n")
        print("Videos de ese genero :")
        pintarNom(buscador1.bus_tag_vid('genero', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
def pintarBusI(t):
    os.system('cls')
    "funcion que crea y pinta el menu de busqueda para las imagenes"
    print("Buscar por : ")
    print("1. Nombre")
    print("2. Autor")
    print("3. Fecha")
    print("4. Genero")
    bb = int(input("Escoja un opción : \n"))
    os.system('cls')

    if bb==1:
        c = input("Escriba el nombre: \n")
        print("Imagen con este nombre :")
        pintarNom(buscador1.bus_tag_fot('nombre',c) )
        c = input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)

    elif bb==2:
        c = input("Escriba el autor: \n")
        print("Imagenes de ese autor :")
        pintarNom(buscador1.bus_tag_fot('autor', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
    elif bb==3:
        c = input("Escriba el Fecha: \n")
        print("Imagenes de ese Fecha :")
        pintarNom(buscador1.bus_tag_fot('fecha', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)
    elif bb==4:
        c = input("Escriba el Genero \n")
        print("Imagenes de ese genero :")
        pintarNom(buscador1.bus_tag_fot('genero', c))
        c= input("Escriba el nombre del archivo para ver detalles: \n")
        n = buscador1.bus_nombre(c)
        pintarDet(n)
        d = input("¿Desea editar? S / N  ")
        if d.upper() == "S":
            eti = str(input("¿Que atributo desea editar?"))
            txt = str(input("Escriba el cambio  "))
            xml1.editar(c, eti.lower(), txt.capitalize())
            multimediaW(t)
        # print("edito")
        else:
            multimediaW(t)

def pintarAlbM(t):
    os.system('cls')
    "funcion que crea y pinta el menu de albumes para la musica"
    print("1. Ver Albumes")
    print("2. Crear Albumes")
    print("3. Atras")
    b = int(input("Escoja un opción : \n"))
    os.system('cls')
    if b==1:
        print("-------------ALBUMES DE MUSICA-----------")
        pintarNom(buscador1.tag_mus('album'))
        bb=input("Ingrese el album que desea ver : \n")
        print ("-------------"+bb+"-------------")
        pintarNom(buscador1.bus_tag_mus('album',bb))
        c=str(input("¿Quiere modificar el album?  S / N \n"))
        if c.upper()=="S":
            print("1. Agregar musica")
            print("2. Eliminar musica")
            bt = int(input("Escoja un opción : \n"))
            if bt==1:
                pintarNom(definir1.musica())
                name=input("Nombre del archivo que desea agregar al album : \n")
                xml1.editar(name,'album',bb)
                pintarAlbM(t)
            else:
                name=input("Nombre del archivo que desea eliminar del album : \n")
                xml1.editar(name,'album','desconocido')
                pintarAlbM(t)
        else:
            multimediaW(t)
    elif b == 2:
        albumn = str(input("Nombre del album a crear : \n"))
        # crear album
        print("Imagenes que puede agregar")
        pintarNom(definir1.musica())
        bc = " "
        bc = input("Escriba nombre del archivo que va agregar : \n")
        while bc != "":
            xml1.editar(bc, 'album', albumn)
            print("Cerrar Bucle oprima enter")
            bc = input("Escriba nombre del archivo que va agregar : \n")
        pintarAlbM(t)
    else:
        multimediaW(t)

def pintarAlbV(t):
    os.system('cls')
    "funcion que crea y pinta el menu de albumes para los videos"
    print("1. Ver Albumes")
    print("2. Crear Albumes")
    print("3. Atras")
    b = int(input("Escoja un opción : \n"))
    os.system('cls')
    if b==1:
        print("-------------ALBUMES DE VIDEOS-----------")
        pintarNom(buscador1.tag_vid('album'))
        bb=input("Ingrese el album que desea ver : \n")
        print ("-------------"+bb+"-------------")
        pintarNom(buscador1.bus_tag_vid('album',bb))
        c=str(input("¿Quiere modificar el album?  S / N \n"))
        if c.upper()=="S":
            print("1. Agregar video")
            print("2. Eliminar video")
            bt = int(input("Escoja un opción : \n"))
            if bt==1:
                pintarNom(definir1.videos())
                name=input("Nombre del archivo que desea agregar al album : \n")
                xml1.editar(name,'album',bb)
                pintarAlbV(t)
            else:
                name=input("Nombre del archivo que desea eliminar del album : \n")
                xml1.editar(name,'album','desconocido')
                pintarAlbV(t)
        else:
            multimediaW(t)
    elif b == 2:
        albumn = str(input("Nombre del album a crear : \n"))
        # crear album
        print("Imagenes que puede agregar")
        pintarNom(definir1.videos())
        bc = " "
        bc = input("Escriba nombre del archivo que va agregar : \n")
        while bc != "":
            xml1.editar(bc, 'album', albumn)
            print("Cerrar Bucle oprima enter")
            bc = input("Escriba nombre del archivo que va agregar : \n")
        pintarAlbV(t)
    else:
        multimediaW(t)



def pintarAlbI(t):
    os.system('cls')
    "funcion que crea y pinta el menu de albumes para las imagenes"
    print("1. Ver Albumes")
    print("2. Crear Albumes")
    print("3. Atras")
    b = int(input("Escoja un opción : \n"))
    os.system('cls')
    if b==1:
        print("-------------ALBUMES DE IMAGENES-----------")
        pintarNom(buscador1.tag_fot('album'))
        bb=input("Ingrese el album que desea ver : \n")
        print ("-------------"+bb+"-------------")
        pintarNom(buscador1.bus_tag_fot('album',bb))
        c=str(input("¿Quiere modificar el album?  S / N \n"))
        if c.upper()=="S":
            print("1. Agregar imagen")
            print("2. Eliminar imagen")
            bt = int(input("Escoja un opción : \n"))
            if bt==1:
                pintarNom(definir1.fotos())
                name=input("Nombre del archivo que desea agregar al album : \n")
                xml1.editar(name,'album',bb)
                pintarAlbI(t)
            else:
                name=input("Nombre del archivo que desea eliminar del album : \n")
                xml1.editar(name,'album','desconocido')
                pintarAlbI(t)
        else:
            multimediaW(t)
    elif b==2:
        albumn=str(input("Nombre del album a crear : \n"))
        #crear album
        print("Imagenes que puede agregar")
        pintarNom(definir1.fotos())
        bc=" "
        bc = input("Escriba nombre del archivo que va agregar : \n")
        while bc!="":
            xml1.editar(bc,'album',albumn)
            print("Cerrar Bucle oprima enter")
            bc = input("Escriba nombre del archivo que va agregar : \n")
        pintarAlbI(t)
    else:
        multimediaW(t)

def pintarListM(t):
    os.system('cls')
    "funcion que crea y pinta el menu de listas para la musica"
    print("-----------------LISTAS MUSICA----------------------")
    print("1. Crear Listas")
    print("2. Ver Listas")
    print("3. Atras")
    b = int(input("Escoja un opción : \n"))
    os.system('cls')
    if b==1:
        nom=input("Ingrese al nombre de la lista nueva: \n")
        xml1.cre_list(1,nom)
        print("Se ha creado la lista "+nom)
        bg=input("¿Desea agregar musica a la lista? S / N ")
        if bg.upper()=='S':
            pintarNom(definir1.musica())
            bgg=input("Ingrese el nombre del archivo a agregar :")
            while bgg!="":
                xml1.cre_cancion(1,nom,bgg)
                print("Cerrar Bucle oprima enter")
                bgg = input("Ingrese el nombre del archivo a agregar :")
                pintarListM(t)
        else:
            pintarListM(t)
    elif b==2:
        print("------ -----LISTAS DE MUSICA-----------")
        pintarNom(xml1.listas(1))
        nom=input("Ingrese el nombre de la lista que desea ver : \n")
        print("------------"+nom+"-------------")
        pintarNom(xml1.lis_list(1,nom))
        bg = input("¿Desea editar esta lista? S / N ")
        if bg.upper()=='S':
            print("1. Agregar Cancion")
            print("2. Eliminar Cancion")
            print("3. Eliminar lista")
            bk = int(input("Escoja un opción : \n"))
            if bk==1:
                pintarNom(definir1.musica())
                bgg = input("Ingrese el nombre del archivo a agregar :")
                while bgg != "":
                    xml1.cre_cancion(1, nom, bgg)
                    print("Cerrar Bucle oprima enter")
                    bgg = input("Ingrese el nombre del archivo a agregar :")
                pintarListM(t)
            elif bk==2:
                pintarNom(xml1.lis_list(1,nom))
                bgg = input("Ingrese el nombre del archivo a eliminar :")
                while bgg != "":
                    xml1.eli_cancion(1, nom, bgg)
                    print("Cerrar Bucle oprima enter")
                    bgg = input("Ingrese el nombre del archivo a eliminar :")
                pintarListM(t)
            elif bk==3:
                xml1.eli_list(1,nom)
                print("Se ha eliminado la lista "+nom)
                pintarListM(t)
        else:
            pintarListM(t)
    else:
        multimediaW(t)
def pintarListV(t):
    os.system('cls')
    "funcion que crea y pinta el menu de listas para los videos"
    print("-----------------LISTAS VIDEOS----------------------")
    print("1. Crear Listas")
    print("2. Ver Listas")
    print("3. Atras")
    b = int(input("Escoja un opción : \n"))
    os.system('cls')
    if b==1:
        nom=input("Ingrese al nombre de la lista nueva: \n")
        xml1.cre_list(0,nom)
        print("Se ha creado la lista "+nom)
        bg=input("¿Desea agregar videos a la lista? S / N ")
        if bg.upper()=='S':
            pintarNom(definir1.videos())
            bgg=input("Ingrese el nombre del archivo a agregar :")
            while bgg!="":
                xml1.cre_cancion(0,nom,bgg)
                print("Cerrar Bucle oprima enter")
                bgg = input("Ingrese el nombre del archivo a agregar :")
                pintarListV(t)
        else:
            pintarListV(t)
    elif b==2:
        print("------ -----LISTAS DE VIDEOS-----------")
        pintarNom(xml1.listas(0))
        nom=input("Ingrese el nombre de la lista que desea ver : \n")
        print("------------"+nom+"-------------")
        pintarNom(xml1.lis_list(0,nom))
        bg = input("¿Desea editar esta lista? S / N ")
        if bg.upper()=='S':
            print("1. Agregar Video")
            print("2. Eliminar Video")
            print("3. Eliminar lista")
            bk = int(input("Escoja un opción : \n"))
            if bk==1:
                pintarNom(definir1.videos())
                bgg = input("Ingrese el nombre del archivo a agregar :")
                while bgg != "":
                    xml1.cre_cancion(0, nom, bgg)
                    print("Cerrar Bucle oprima enter")
                    bgg = input("Ingrese el nombre del archivo a agregar :")
                pintarListV(t)
            elif bk==2:
                pintarNom(xml1.lis_list(0,nom))
                bgg = input("Ingrese el nombre del archivo a eliminar :")
                while bgg != "":
                    xml1.eli_cancion(0, nom, bgg)
                    print("Cerrar Bucle oprima enter")
                    bgg = input("Ingrese el nombre del archivo a eliminar :")
                pintarListV(t)
            elif bk==3:
                xml1.eli_list(0,nom)
                print("Se ha eliminado la lista "+nom)
                pintarListV(t)
        else:
            pintarListV(t)
    else:
        multimediaW(t)

def pintarListI(t):
    os.system('cls')
    "funcion que crea y pinta el menu de listas para las imagenes"
    print("-----------------LISTAS IMAGENES----------------------")
    print("1. Crear Listas")
    print("2. Ver Listas")
    print("3. Atras")
    b = int(input("Escoja un opción : \n"))
    os.system('cls')
    if b==1:
        nom=input("Ingrese al nombre de la lista nueva: \n")
        xml1.cre_list(2,nom)
        print("Se ha creado la lista "+nom)
        bg=input("¿Desea agregar imagenes a la lista? S / N ")
        if bg.upper()=='S':
            pintarNom(definir1.fotos())
            bgg=input("Ingrese el nombre del archivo a agregar :")
            while bgg!="":
                xml1.cre_cancion(2,nom,bgg)
                print("Cerrar Bucle oprima enter")
                bgg = input("Ingrese el nombre del archivo a agregar :")
                pintarListI(t)
        else:
            pintarListI(t)
    elif b==2:
        print("------ -----LISTAS DE IMAGENES-----------")
        pintarNom(xml1.listas(2))
        nom=input("Ingrese el nombre de la lista que desea ver : \n")
        print("------------"+nom+"-------------")
        pintarNom(xml1.lis_list(2,nom))
        bg = input("¿Desea editar esta lista? S / N ")
        if bg.upper()=='S':
            print("1. Agregar Imagen")
            print("2. Eliminar Imagen")
            print("3. Eliminar lista")
            bk = int(input("Escoja un opción : \n"))
            if bk==1:
                pintarNom(definir1.fotos())
                bgg = input("Ingrese el nombre del archivo a agregar :")
                while bgg != "":
                    xml1.cre_cancion(2, nom, bgg)
                    print("Cerrar Bucle oprima enter")
                    bgg = input("Ingrese el nombre del archivo a agregar :")
                pintarListI(t)
            elif bk==2:
                pintarNom(xml1.lis_list(2,nom))
                bgg = input("Ingrese el nombre del archivo a eliminar :")
                while bgg != "":
                    xml1.eli_cancion(2, nom, bgg)
                    print("Cerrar Bucle oprima enter")
                    bgg = input("Ingrese el nombre del archivo a eliminar :")
                pintarListI(t)
            elif bk==3:
                xml1.eli_list(2,nom)
                print("Se ha eliminado la lista "+nom)
                pintarListI(t)
        else:
            pintarListI(t)
    else:
        multimediaW(t)

if __name__ == '__main__':
    mainW()
