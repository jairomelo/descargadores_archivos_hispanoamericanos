# -*- coding: utf-8 -*-

import os
import time
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup

from plataforma import navegador
from reconex import requests_retry_session

rutabase = "https://archivos.gob.mx/guiageneral"

local = os.getcwd()


def imagenes(url):
    browser = navegador()
    browser.get(url)
    time.sleep(10)

    ultimaPag = browser.find_element_by_xpath('/html/body/center[3]/div/a[12]')
    ultimaPag.click()

    currentURL = urlparse(browser.current_url)
    numer = currentURL.query[20:22]
    code = browser.current_url.split('=')[4]

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
            nom_file = ruta2img.split("/")[7]
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
