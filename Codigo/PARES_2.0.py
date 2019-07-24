#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests, time, os
import reconex # Intento de solución de errores de conexión


#########################################################################

ident = input('Ingresar número del expediente: ')

num_imgs = input('cantidad de imágenes: ')
rango = int(num_imgs)/8

#########################################################################

host = 'http://pares.mcu.es'
ruta_entrada = '/ParesBusquedas20/catalogo/show/{}'.format(ident)
url_entrada = '{}{}'.format(host, ruta_entrada)

browser = webdriver.Chrome()
browser.get(url_entrada)

#########################################################################

soup = BeautifulSoup(browser.page_source, 'html.parser')
imgs = soup.select("div.thumbnail img")

rutas = []

#primapágina

for img in imgs:
	obtener = "{}{}".format(host, img["src"])
	rutas.append(obtener)

#resto de páginas
for i in range(int(rango)):
	i = browser.find_element_by_xpath('//*[@id="botonMasPeq"]')
	i.click()
	time.sleep(1)
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	imgs = soup.select("div.thumbnail img")
	for img in imgs:
		obtener = "{}{}".format(host, img["src"])
		rutas.append(obtener)

print(rutas) # Línea sólo para desarrollo

browser.quit()

#########################################################################

if not os.path.exists(ident):
	os.makedirs(ident)

cadenas = str(rutas)
encadenado = ''.join(cadenas).replace('[\'','').replace('\']',',').replace('&txt_transformacion=0','').replace('\'','').replace('&txt_contraste=0', '&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0')
mi_cadena = encadenado.split(",")
print(mi_cadena) # Línea sólo para desarrollo

#########################################################################

from datetime import timedelta # solo para desarrollo

inicio_loop = time.time() # Desarrollo : tiempo que toma en ejecutarse el programa
for i in range(len(rutas)):
	start = time.time()
	if not os.path.exists("{}/{}.jpg".format(ident, i+1)):
		s = requests.Session()
		read = reconex.requests_retry_session(session=s).get(url_entrada) # Intento de solución de errores de conexión
		url_descarga = mi_cadena[i]
		read = reconex.requests_retry_session(session=s).get(url_descarga) # Intento de solución de errores de conexión
		with open("{}/{}.jpg".format(ident, i+1), 'wb') as handler:
			handler.write(read.content)
			print("Descargando la imagen {}.jpg de {}".format(i+1, num_imgs))
			lapso = (time.time() - start) # Desarrollo : tiempo que toma en ejecutarse el programa
			print("Descargada en {} segundos".format(lapso)) # Desarrollo : tiempo que toma en ejecutarse el programa
			time.sleep(1)

lapso_loop = (time.time() - inicio_loop) # Desarrollo : tiempo que toma en ejecutarse el programa
horminsec = str(timedelta(seconds=lapso_loop))

print("Descargadas {} imágenes en {}".format(num_imgs,horminsec))