import urllib.request
import os

enlace = input('Enlace del número del periódico. <br /> Pegue la liga solamente hasta el signo de % \(ejemplo: http://consulta.archivogeneral.gov.co/ConsultaWeb/assets/image?id=\)<br /> : ')
directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
init = input('Número de la imágen inicial: ')
fin = input('Número de la página final: ')

os.makedirs(directorio)

init_i = int(init)
fin_i = int(fin)

url_base = "%s{}" % enlace
lista = range(init_i,fin_i)

rango = len(lista)

for i in range(rango):
    url = url_base.format(lista[i])
    down = urllib.request.urlretrieve(url, "%s/%s.jpg" % (directorio, i))
