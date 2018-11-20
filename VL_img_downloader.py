import urllib.request
import wget, os

directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
init = input('Número de la imágen inicial: ')
fin = input('Número de la página final: ')

os.makedirs(directorio)

init_i = int(init)
fin_i = int(fin)

url_base = "http://hemeroteca.vanguardia.com/hemeroteca/public/periodico/img_pdf/vl/1953/1953-11-02/vl19531102%{}.jpg"
lista = range(init_i,fin_i)

rango = len(lista)

for i in range(rango):
    url = url_base.format(lista[i])
    down = urllib.request.urlretrieve(url, "%s/%s.jpg" % (directorio, i))
