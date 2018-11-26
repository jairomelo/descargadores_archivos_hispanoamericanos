from selenium import webdriver
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

s = requests.Session()

#########################################################################

r = s.get(url_entrada)
soup = BeautifulSoup(r.content, 'html.parser')
imgs = soup.select("div.thumbnail img")

rutas = []

def get_srcs():
	for img in imgs:
		obtener = "{}{}".format(host, img["src"])
		rutas.append(obtener)

#primapágina
get_srcs()
#resto de páginas
for i in range(int(rango)):
	i = browser.find_element_by_xpath('//*[@id="botonMasPeq"]')
	i.click()
	time.sleep(5)
	get_srcs()

#########################################################################

if not os.path.exists(ident):
	os.makedirs(ident)

for i in range(len(rutas)):
	cadenas = str(rutas)
	encadenado = ''.join(cadenas).replace('[\'','').replace('\']',',').replace('&txt_transformacion=0','').replace('\'','')
	mi_cadena = encadenado.split(",")
	url_descarga = mi_cadena[i]
	read = s.get(url_descarga)
	with open("%s/%s.jpg" % (ident, i), 'wb') as handler:
		handler.write(read.content)
		time.sleep(1)

#########################################################################

browser.quit()