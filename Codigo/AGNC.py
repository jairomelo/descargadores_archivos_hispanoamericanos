import os
import time
import urllib.request

enlace = "http://consulta.archivogeneral.gov.co/ConsultaWeb/assets/image?id="
directorio = input('Ingresa el nombre de la carpeta para guardar las imágenes: ')
init = input('Número de la imagen inicial: ')
fin = input('Número de la página final: ')

init_i = int(init)
fin_i = int(fin) + 1

lista = range(init_i, fin_i)

if not os.path.exists(directorio):
    os.makedirs(directorio)

print("Se van a descargar {} imágenes".format(fin_i - init_i))

for i in range(len(lista)):
    url = "{}{}".format(enlace, lista[i])
    print("\r" + "Descargando img {}".format(i + 1) + ".", end="")
    try:
        if not os.path.exists("{}/{}.jpg".format(directorio, i + 1)):
            urllib.request.urlretrieve(url, "{}/{}.jpg".format(directorio, i + 1))
            time.sleep(3)
        else:
            pass
    except urllib.error.HTTPError as err:
        print("No se pudo descargar la img {} del enlace {}".format(i + 1, url) + "\n" + "ERROR {}".format(err.code))
