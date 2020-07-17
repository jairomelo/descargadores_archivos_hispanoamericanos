#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import sys

import requests

try:
    from bs4 import BeautifulSoup
except ImportError:
    # Verifica la instalación de los módulos requeridos
    print((os.linesep * 2).join(["No fue posible importar el módulo:",
                                 str(sys.exc_info()[1]),
                                 "Debe instalarlo para poder correr el programa [Ver ayuda en: https://programminghistorian.org/es/lecciones/instalar-modulos-python-pip]",
                                 "Saliendo del programa..."]))
    sys.exit(-2)

try:
    import reconex  # Intento de solución de errores de conexión
except ImportError:
    # Verifica que se encuentren disponibles los archivos adicionales
    print(str(sys.exc_info()[1]),
          "No se encontró el archivo 'reconex.py'. Asegúrese de haberlo descargado y que esté en la carpeta principal del programa")
    sys.exit(-2)

#########################################################################

print(
    "¿Qué desea descargar? \n Contribuciones de usuarios [cdu] \n Datos agregados [da] \n Niveles territoriales [nt] \n mapas [mps]")

while True:
    dir1 = input('>> ')
    if dir1 == "cdu":
        dir2 = "Contribuciones_de_usuarios/"
        break
    elif dir1 == "da":
        dir2 = "Datos%20agregados/"
        break
    elif dir1 == "nt":
        print("\n Nivel Territorial \n")
        print(
            "Seleccione un nivel territorial: \n Arzobispado [Az] \n Audiencia [Au] \n Extranjero [Ex] \n Fronteras [Fr] \n Intendencia [Int] \n Jurisdicción [Jd] \n Obispado [Ob] \n Partido [Prt] \n Principal [Ppal] \n Provincia [Pva] \n Provincia Mayor [PvaM] \n Provincia menor [Pvam] \n Señorío [Sro] \n Virreinato [Vto]")
        dir1_1 = input('{}>> '.format(dir1))
        if dir1_1 == "Az":
            dir2 = "Niveles_territoriales/Arzobispado/"
            break
        if dir1_1 == "Au":
            dir2 = "Niveles_territoriales/Audiencia/"
            break
        if dir1_1 == "Ex":
            dir2 = "Niveles_territoriales/Extranjero/"
            break
        if dir1_1 == "Fr":
            dir2 = "Niveles_territoriales/Fronteras/"
            break
        if dir1_1 == "Int":
            dir2 = "Niveles_territoriales/Intendencia/"
            break
        if dir1_1 == "Jd":
            dir2 = "Niveles_territoriales/Jurisdiccion/"
            break
        if dir1_1 == "Ob":
            dir2 = "Niveles_territoriales/Obispado/"
            break
        if dir1_1 == "Prt":
            dir2 = "Niveles_territoriales/Partido/"
            break
        if dir1_1 == "Ppal":
            dir2 = "Niveles_territoriales/Principal/"
            break
        if dir1_1 == "Pva":
            dir2 = "Niveles_territoriales/Provincia/"
            break
        if dir1_1 == "PvaM":
            dir2 = "Niveles_territoriales/Provincia_mayor/"
            break
        if dir1_1 == "Pvam":
            dir2 = "Niveles_territoriales/Provincia_menor/"
            break
        if dir1_1 == "Sro":
            dir2 = "Niveles_territoriales/Senorio/"
            break
        if dir1_1 == "Vto":
            dir2 = "Niveles_territoriales/Virreinato/"
            break
        else:
            print("Error al indicar el directorio a descargar. \n Ejemplo: {}>> Az".format(dir1))
            input("ENTER para reintentar")
    else:
        print("Error al indicar el directorio a descargar. \n Ejemplo: >> cdu")
        input("ENTER para reintentar")

#########################################################################

host = 'https://www.hgis-indias.net'
ruta_entrada = '/downloads/{}'.format(dir2)
url_entrada = '{}{}'.format(host, ruta_entrada)

s = requests.Session()
read = reconex.requests_retry_session(session=s).get(url_entrada, verify=False)  # ¡Esto no debe hacerse!

#########################################################################

soup = BeautifulSoup(read, 'html.parser')

print(soup)

time.sleep(5)
