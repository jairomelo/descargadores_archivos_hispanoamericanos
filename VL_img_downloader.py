import urllib.request
import os

enlace_base = "http://hemeroteca.vanguardia.com/hemeroteca/public/periodico/img_pdf/vl/"

fecha_ini = input('Fecha inicial (YYYY-MM-DD): ')

#string manipulation

año_ini = fecha_ini[0:4]
mes_ini = fecha_ini[5:7]
dia_ini = fecha_ini[8:10]

# formato url

url_busqueda = "{}{}/{}-{}-{}/vl{}{}{}%".format(enlace_base,año_ini,año_ini,mes_ini,dia_ini,año_ini,mes_ini,dia_ini)

if not os.path.exists(fecha_ini):
	os.makedirs(fecha_ini)

init_i = 201
fin_i = 210

lista = range(init_i,fin_i)

for i in range(len(lista)):
    url = "{}{}.jpg".format(url_busqueda, lista[i])
    down = urllib.request.urlretrieve(url, "{}/{}.jpg".format(fecha_ini, i))
