from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests, time, os

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
	time.sleep(5)
	soup = BeautifulSoup(browser.page_source, 'html.parser')
	imgs = soup.select("div.thumbnail img")
	for img in imgs:
		obtener = "{}{}".format(host, img["src"])
		rutas.append(obtener)


print(rutas)

#########################################################################

if not os.path.exists(ident):
	os.makedirs(ident)

s = requests.Session()
read = s.get(url_entrada)

for i in range(len(rutas)):
	cadenas = str(rutas)
	encadenado = ''.join(cadenas).replace('[\'','').replace('\']',',').replace('&txt_transformacion=0','').replace('\'','').replace('&txt_contraste=0', '&txt_zoom=10&txt_contraste=0&txt_polarizado=&txt_brillo=10.0&txt_contrast=1.0')
	mi_cadena = encadenado.split(",")
	print(mi_cadena)
	url_descarga = mi_cadena[i]
	read = s.get(url_descarga)
	with open("{}/{}.jpg".format(ident, i), 'wb') as handler:
		handler.write(read.content)
		time.sleep(1)

#########################################################################

browser.quit()