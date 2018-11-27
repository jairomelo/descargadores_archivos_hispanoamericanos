import urllib.request
import os

enlace = "http://consulta.archivogeneral.gov.co/ConsultaWeb/assets/image?id="
directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
init = input('Número de la imagen inicial: ')
fin = input('Número de la página final: ')

init_i = int(init)
fin_i = int(fin) + 1

url_base = "%s{}" % enlace
lista = range(init_i,fin_i)

os.makedirs(directorio)

for i in range(len(lista)):
    url = url_base.format(lista[i])
    down = urllib.request.urlretrieve(url, "%s/%s.jpg" % (directorio, i))
