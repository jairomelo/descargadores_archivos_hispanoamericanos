#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Este truco funciona desde localhost. 
Es necesario, descargar el resultado de la búsqueda en un directorio local. La fuentes será '/portadacatalogogeneral.html'
Al parecer no es necesario cambiar el 'host', pero en caso de error puede estar ahí el problema.
'''


from bs4 import BeautifulSoup
import urllib.request
import requests, time, os
import reconex

ident = input("NOMBRE_ARCHIVO_LOCAL: ") # ejemplo: "ANT_4_942-993" - Cambiar con cada descarga NO OLVIDAR!!!!!!!!!!!!!!!
localhost = "http://localhost/ne/"
source =  "{}{}.html".format(localhost,ident)

################################################
# esta función regresa una lista que luego usaremos para descargar las imágenes
def lista(selector,sopa,oe='e'):
	''' 
	selector: el selector CSS para el elemento
	sopa = soup
	oe = 'o' para que retire el encabezado en las #TR2 '''
	idlista = []

	for parras in sopa.select(selector): 
		obtener = "{}{}".format(host, parras.text)
		idlista.append(obtener)

	if oe == 'o':
		idlista.remove('{}Nombre Imágen'.format(host))

	return idlista

def descarga(lista,rv):
	for i in range(len(lista)):
		s = requests.Session()
		url_descarga = lista[i]
		read = reconex.requests_retry_session(session=s).get(url_descarga)
		with open("{}/{}-{}.jpg".format(ident, i+1,rv), 'wb') as handler:
			handler.write(read.content)
			time.sleep(1)
			print("descargada la imagen {}/{}-{}.jpg".format(ident, i+1,rv))

################################################

url = urllib.request.urlopen(source)
soup = BeautifulSoup(url, 'html.parser')

################################################
# Fuente externa

for idhos in soup.select('body > form > fieldset > font > font > table > tbody > tr:nth-child(4) > td:nth-child(2) > p'):
	idhost = idhos.text

host = "http://negrosyesclavos.archivogeneral.gov.co:8181/nyssinimag/kwdp/portal/apps/php/kwimages/{}/".format(idhost)
################################################

if not os.path.exists(ident):
	os.makedirs(ident)

descarga(lista('#TR1 > td:nth-child(3) > p',soup),'r')
descarga(lista('#TR2 > td:nth-child(3) > p',soup,'o'),'v')

print("finalizada la descarga")