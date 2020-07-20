# -*- coding: utf-8 -*-

import os
import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from selenium.common.exceptions import NoSuchElementException

from plataforma import navegador
from reconex import requests_retry_session

rutabase = "https://archivos.gob.mx/guiageneral"

local = os.getcwd()

'''
Función para regresar la cantidad de páginas
Si la cantidad es menor a 10 regresa ese número
'''


def cantidad_pags(selenium_session):
    try:
        ultima_pag = selenium_session.find_element_by_xpath('/html/body/center[3]/div/a[12]')
        ultima_pag.click()
        actual_url = urlparse(selenium_session.current_url)
        return actual_url.query[20:22]
    except NoSuchElementException:
        return 10


def codigo_legajo(selenium_session):
    try:
        return selenium_session.current_url.split('=')[4]
    except IndexError:
        return selenium_session.current_url.split('=')[1]


def nombre_archivo(ruta):
    separar = ruta.split("/")
    largo = int(len(separar))
    return ruta.split("/")[largo - 1]


def imagenes(url):
    browser = navegador()
    browser.get(url)
    time.sleep(10)

    numer = cantidad_pags(browser)
    code = codigo_legajo(browser)

    for i in range(int(numer) + 1):
        nova_url = "{}/visorimg/visorimg.php?page={}&item=0&max={}&CodR={}".format(rutabase, i, numer, code)
        print(nova_url)

        browser.get(nova_url)

        salsa = BeautifulSoup(browser.page_source, 'html.parser')
        sopa = salsa.select('div img',
                            class_='fotorama__loaded--img')
        print(sopa)
        if not os.path.exists('{}/descargas/{}'.format(local, code)):
            os.makedirs('{}/descargas/{}'.format(local, code))

        for imgs in sopa:
            ruta2img = imgs['src'].replace('..', '')
            print(ruta2img)
            nom_file = nombre_archivo(ruta2img)
            ruta2imgfull = rutabase + ruta2img
            print(ruta2imgfull)
            print(nom_file)
            s = requests.Session()
            read = requests_retry_session(session=s).get(ruta2imgfull)
            if not os.path.isfile("{}/descargas/{}/{}".format(local, code, nom_file)):
                with open("{}/descargas/{}/{}".format(local, code, nom_file), 'wb') as handler:
                    handler.write(read.content)
                    print("descargando la imagen {}".format(nom_file))

    browser.quit()
